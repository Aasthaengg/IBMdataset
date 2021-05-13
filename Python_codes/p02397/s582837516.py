while True:
	[a,b]=raw_input().split()
	x=int(a)
	y=int(b)
	if x==y==0:break
	if x<=y:
		print a,b
	else:
		print b,a