while True:
	try:
		n = map(int, raw_input().split())
		a = max(n) 
		b = min(n)
		ab = a * b
		while b != 0 :
			c = a % b
			a = b
			b = c
		print str(a) + " " + str(ab / a)
	except EOFError:
		break