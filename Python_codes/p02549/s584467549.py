n, k = map(int, input().split())
LR = [[*map(int, input().split())] for _ in range(k)]

MOD = 998244353
dp = [0]*n  # [0,n-1]
dp[0] = 1 # init
dp[1] = -1  # for Cumulative sum

for i in range(n): # i:[0,n-1]
    if i > 0: dp[i] += dp[i-1] # Cumulative sum
    for l, r in LR:
        if i+l < n:
            dp[i+l] += dp[i]
            dp[i+l] %= MOD
        if i+r+1 < n:
            dp[i+r+1] -= dp[i]
            dp[i+r+1] %= MOD

print((dp[n-1] + MOD) % MOD)
