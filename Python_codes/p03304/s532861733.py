n,m,d=map(int,input().split())
if n>=2*d and d:
	print(2*(n-d)*(m-1)/(n*n))
elif n>=d:
	print((m-1)/n)
else:
	print(0)