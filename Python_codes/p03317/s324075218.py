n,k=map(int,input().split())
if n<=k:
	print(1)
else:
	n=n-k
	r=list(map(int,input().split()))
	if n%(k-1)==0:print(1+n//(k-1))
	else:print(2+n//(k-1))