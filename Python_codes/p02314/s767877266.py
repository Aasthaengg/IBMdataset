n,m,*L=map(int,open(0).read().split())
dp=list(range(n+1))
for c in L:
	for j in range(c,n+1):
		dp[j]=min(dp[j],dp[j-c]+1)
print(dp[n])
