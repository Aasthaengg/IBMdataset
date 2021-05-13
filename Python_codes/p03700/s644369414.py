_,a,b,*H=map(int,open(0).read().split())
l,r=0,10**9
while r-l>1:
	m=(l+r)//2
	if-sum(min(0,(h-m*b)//(b-a))for h in H)>m:l=m
	else:r=m
print(r)
