while True:
	n = map(int,raw_input().split(' '))
	if n[0] == 0 and n[1] == 0:
		break
	n.sort()
	x = n[0]
	y = n[1]
	print x,y