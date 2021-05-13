n = int(input())
c = [int(input()) for i in range(n)]
MOD = 10**9 + 7

dp = [0]*(n+1)
dp[0] = 1
memo = {}
for i in range(n):
    if c[i] not in memo:
        memo[c[i]] = i
        dp[i+1] = dp[i]
    else:
        if c[i]==c[i-1]:
            dp[i+1] = dp[i]
            memo[c[i]] = i
            continue
        # memo[c[i]]からiの区間を変えるとき
        dp[i+1] += dp[memo[c[i]]+1]
        # memo[c[i]]からiの区間を変えないとき
        dp[i+1] += dp[i]
        
        memo[c[i]] = i
        dp[i+1] %= MOD
print(dp[-1] % MOD)