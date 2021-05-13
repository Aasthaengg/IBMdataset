while True:
	x = input()
	if x == '0':
		break
	s=0
	for i in range(len(x)):
		s+=int(x[i])
	print(s)