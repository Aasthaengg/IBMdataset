l = input()
mod = 10**9+7
n = len(l)
dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    
    # a+b==0 (両方に0)
    if l[i]=='0':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][1] = (dp[i][0]+dp[i][1]) % mod
    
    # a+b==1 (片方に0,片方に1)
    if l[i]=='0':
        dp[i+1][1] += dp[i][1]*2
        dp[i+1][1] %= mod
    else:
        dp[i+1][0] += dp[i][0]*2
        dp[i+1][1] += dp[i][1]*2
        dp[i+1][0] %= mod
        dp[i+1][1] %= mod

ans = (dp[n][0]+dp[n][1])%mod
print(ans) 