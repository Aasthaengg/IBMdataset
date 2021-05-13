n=int(input())
c=[int(input()) for _ in range(n)]
mod=10**9+7

dp=[0]*(n+1)

dp[0]=1
last=[-1]*(2*10**5+1)
last[c[0]]=0

for i in range(1,n):
    if c[i]==c[i-1] or last[c[i]]==-1:
        dp[i]=dp[i-1]
    else:
        dp[i]=(dp[i-1]+dp[last[c[i]]])%mod
    last[c[i]]=i

print(dp[n-1])
