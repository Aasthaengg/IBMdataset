while 1:
	n = input().split()
	a = int(n[0])
	b = int(n[1])
	if a == 0 and b == 0:
		break
	if a > b:
		bf = a
		a = b
		b = bf
	print(str(a) + " " + str(b))