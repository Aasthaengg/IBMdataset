while True:
	x,y=map(int, raw_input().split())
	if x==0 and y==0:
		break
	else:
		if x>=y:
			print y,x
		else:
			print x,y