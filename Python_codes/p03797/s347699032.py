n,m=map(int,input().split())
ans=0
if n*2<=m:
	ans+=n
	m-=2*n
	ans+=int(m/4)
	print(ans)
else:
	ans+=int(m/2)
	print(ans)