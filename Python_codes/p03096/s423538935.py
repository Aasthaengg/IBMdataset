mod=10**9+7
import sys
input=sys.stdin.readline
n=int(input())
c=[int(input())for i in range(n)]
last=[-1]*max(c)
last[c[0]-1]=0
dp=[0]*n
dp[0]=1
for i in range(1,n):
	dp[i]=dp[i-1]
	if c[i-1]!=c[i] and last[c[i]-1]!=-1:
		dp[i]+=dp[last[c[i]-1]]
		dp[i]%=mod
	last[c[i]-1]=i
print(dp[-1])