l=input()
mod=10**9+7

# dp[digit][smaller]
# dp[i][j]
dp = [[0 for _ in range(2)] for _ in range(len(l)+1)]
dp[0][0]=1 # smaller:1==False
for i in range(len(l)):
    dp[i+1][1] += (3*dp[i][1])
    if l[i] == "1":
        dp[i+1][1] += dp[i][0]
        dp[i+1][0] += (2*dp[i][0])
    else:
        dp[i+1][0] += dp[i][0]
    dp[i+1][0] %= mod
    dp[i+1][1] %= mod

ans = dp[-1][0] + dp[-1][1]
print(ans % mod)