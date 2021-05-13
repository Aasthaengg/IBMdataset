import collections
n=int(input())
c=[0]+[int(input()) for i in range(n)]
d=collections.defaultdict(int)
mod=10**9+7
dp=[1 for i in range(n+1)]
for i in range(0,n):
    if c[i]==c[i+1]:
        dp[i+1]=dp[i]
    else:
        t=c[i+1]
        dp[i+1]=(dp[i]+d[t])%mod
        d[t]+=dp[i]
        d[t]%=mod
print(dp[n])