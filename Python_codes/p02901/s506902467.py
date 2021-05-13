inf=10**9
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dp=[[inf]*(2**n) for _ in range(m+1)]
def two(i):
	return "0"*(n-len(bin(i)[2:]))+bin(i)[2:]
for i in range(m+1):
	dp[i][0]=0
for i in range(m):
	a,b=map(int,input().split())
	r=0
	c=list(map(int,input().split()))
	for p in c:
		r+=2**(p-1)
	for j in range(2**n):
		x=j|r
		dp[i+1][x]=min(dp[i][j]+a,dp[i][x],dp[i+1][x])
	for j in range(2**n):
		dp[i+1][j]=min(dp[i+1][j],dp[i][j])
print(dp[-1][-1]) if dp[-1][-1]!=inf else print(-1)