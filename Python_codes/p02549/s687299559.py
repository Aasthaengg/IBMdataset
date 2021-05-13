mod = 998244353
n, k = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(k)]
for i in range(k):
    lr[i][1] += 1

dp = [0]*n
dp[0] = 1
for i in range(1,n):
    dp[i] = dp[i-1]
    if i == 1:
        dp[1] = 0
    for l,r in lr:
        if i - l >= 0:
            dp[i] += dp[i-l]
        if i - r >= 0:
            dp[i] -= dp[i-r]
        dp[i] %= mod
print(dp[n-1])