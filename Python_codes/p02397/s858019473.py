while 1:
	a, b = map(int, raw_input().split())
	if a == 0 and b == 0:
		break
	else:
		if a > b:
			print b, a
		else:
			print a, b