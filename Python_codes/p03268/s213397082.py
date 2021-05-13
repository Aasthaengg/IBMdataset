n,k=map(int,input().split())
if k%2!=0:
	x=n//k
	print(x**3)
else:
	x=n//k
	y=(n+(k//2))//k
	print(x**3+y**3)
