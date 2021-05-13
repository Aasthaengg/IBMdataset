n, k = map(int, input().split())
LR = []
for _ in range(k):
    l, r = map(int, input().split())
    LR.append([l, r+1])

MOD = 998244353
dp = [0]*(n+1)  # [0,n]
dp[0] = 1
dp[1] = -1

for i in range(n): # i:[0,n-1]
    if i > 0: dp[i] += dp[i-1]
    for j in range(k):
        l, r = LR[j]
        if i+l < n:
            dp[i+l] += dp[i]
            dp[i+l] %= MOD
        if i+r < n:
            dp[i+r] -= dp[i]
            dp[i+r] %= MOD

print((dp[n-1] + MOD) % MOD)
