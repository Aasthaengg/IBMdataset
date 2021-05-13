a,b,x=map(int,input().split())
if(a>x or a+b<x):
	print('NO')
elif(a+b>=x):
	print('YES')