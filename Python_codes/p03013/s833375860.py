import math
n,m=map(int,input().split())
h=[0 for _ in range(n+1)]
dp=[0 for _ in range(n+1)]
for i in range(m):
	s=int(input())
	h[s]=1
dp[0]=1
if h[1]==1:
	dp[1]=0
else:
	dp[1]=1
for i in range(2,n+1):
	if h[i]==1:
		dp[i]==0
	else:
		dp[i]=dp[i-1]+dp[i-2]
print(dp[n]%1000000007)
