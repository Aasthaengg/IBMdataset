l=list(input())
mod=pow(10,9)+7
n=len(l)

dp=[[0,0] for i in range(n+1)]
dp[0][1]=1
# dp[i][0] 未満確定した物
# dp[i][1] まだ未満確定していない
for i in range(n):
    if l[i]=='1':
        dp[i+1][0]=3*dp[i][0]%mod
        dp[i+1][0]+=dp[i][1]%mod
        dp[i+1][1]+=2*dp[i][1]%mod
    else:
        dp[i+1][0]=3*dp[i][0]%mod
        dp[i+1][1]=dp[i][1]%mod
print((dp[-1][0]+dp[-1][1])%mod)