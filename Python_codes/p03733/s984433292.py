N,T=map(int,input().split())
L=list(map(int,input().split()))
ans=0
for i in range (N-1):
	if L[i+1]-L[i]>T:
		ans+=T
	else:
		ans+=L[i+1]-L[i]
print(ans+T)