while True:
	y,x=map(int, input().split())
	if x==y==0: break
	print(('#'*x+'\n')*y)