while True :
	x = raw_input().split()
	a = int(x[0])
	b = int(x[2])

	if x[1] == '+' :
		print a + b
	elif x[1] == '-' :
		print a - b
	elif x[1] == '*' :
		print  a * b 
	elif x[1] == '/' :
		print a / b
	elif x[1] == '?' :
		break