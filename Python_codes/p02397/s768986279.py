while True:
	x, y = map(int, raw_input().split())
	if x == y ==0:
		break
	elif x > y:
		print "%d %d" % (y,x)
	else:
		print "%d %d" % (x,y)