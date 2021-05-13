n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (n+1);

dp[0] = 1
dp[1] = -1

for i in range(0, n):
    if i>0: dp[i] += dp[i-1]
    dp[i] %= 998244353
    for l,r in lr:
        if i+l > n: continue
        dp[i+l] += dp[i]
        dp[min(n, i+r+1)] -= dp[i]

print(dp[-2] % 998244353)
