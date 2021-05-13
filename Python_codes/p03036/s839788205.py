def bbb(x,r,d):
	return r*x-d

r,d,x=map(int,input().split())
for _ in range(10):
	print(bbb(x,r,d))
	x=bbb(x,r,d)