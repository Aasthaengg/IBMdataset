n,*a=map(int,open(0).read().split())
l=r=x=s=ans=0
while l<n:
	while r<n and x^a[r]==s+a[r]:
		x^=a[r]
		s+=a[r]
		r+=1
		ans+=1
	x^=a[l]
	s-=a[l]
	l+=1
	ans+=r-l
print(ans)