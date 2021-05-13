s = int(input())
if s <= 2:
    print(0)
else:
    dp = [0]*(s+1)
    dp[s] = 1
    mod = 10**9+7
    for i in range(s, 1, -1):
        dp[i-1] += dp[i]
        dp[i-1] %= mod
        if i-3 >= 0:
            dp[i-3] += dp[i]
            dp[i-3] %= mod
    print(dp[0]%mod)
    
