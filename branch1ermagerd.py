def ermagerd(msg):
	temp=""
	for let in msg:
		if let=='a' or let=='e' or let=='i' or let=='u' or let=='o':
			let='er'
		temp+=let
	print temp
if __name__=='__main__':
	ermagerd('hello')