N=int(input())
mod=10**9+7
dp=[0]*N
idx=dict()
idx[int(input())]=0
dp[0]=1
for i in range(1,N):
    C=int(input())
    if C in idx.keys():
        if idx[C]<i-1:
            dp[i]=(dp[idx[C]]+dp[i-1])%mod
        else:
            dp[i]=dp[i-1]
    else:
        dp[i]=dp[i-1]
    idx[C]=i
print(dp[-1])