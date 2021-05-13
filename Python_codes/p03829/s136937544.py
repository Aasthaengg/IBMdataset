n,a,b=map(int,input().split())
aa=list(map(int,input().split()))
ans=0
for i in range(n-1):
	if (aa[i+1]-aa[i])*a>b:
		ans+=b
	else:
		ans+=(aa[i+1]-aa[i])*a
print(ans)