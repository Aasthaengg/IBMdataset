s=list(str(input()))
for i in range(len(s)):
    s[i]=int(s[i])
n=len(s)
mod=10**9+7
dp=[[0 for i in range(2)] for j in range(n+1)]
dp[0][0]=0
dp[0][1]=1
for i in range(n):
    if s[i]==1:
        dp[i+1][0]=(dp[i][0]*3+dp[i][1])%mod
        dp[i+1][1]=dp[i][1]*2%mod
    else:
        dp[i+1][0]=dp[i][0]*3%mod
        dp[i+1][1]=dp[i][1]%mod
print(sum(dp[n])%mod)