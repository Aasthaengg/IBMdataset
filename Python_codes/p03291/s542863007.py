s=input()
l=len(s)
dp=[[0]*4 for i in range(l+1)]
dp[0][0]=1
mod=10**9+7
for i in range(l):
    c = s[i]
    dp[i+1][0]=dp[i][0] 
    dp[i+1][1]=dp[i][1] 
    dp[i+1][2]=dp[i][2] 
    dp[i+1][3]=dp[i][3] 
    if c=="A":
        dp[i+1][1]+=dp[i][0]
    if c=="B":
        dp[i+1][2]=dp[i][2]+dp[i][1] 
    if c=="C":
        dp[i+1][3]=dp[i][3]+dp[i][2]
    if c=="?":
        dp[i+1][0] = (3*dp[i][0])%mod
        dp[i+1][1] = (dp[i][0] + 3*dp[i][1]) % mod
        dp[i+1][2] = (dp[i][1] + 3*dp[i][2]) % mod
        dp[i+1][3] = (dp[i][2] + 3*dp[i][3]) % mod
        

print(dp[-1][3]%mod)