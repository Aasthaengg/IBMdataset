import sys 
while True:
	x,y = map(int,sys.stdin.readline().split())
	if (x==0) & (y==0):
		break
	
	if x<=y:
		print(x,y)
	else:
		print(y,x)