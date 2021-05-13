n, k = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(k)]
dp = [0 for _ in range(n + 1)]
dp[1] = 1
s = 0
mod = 998244353

for i in range(1, n + 1):
    s += dp[i]
    for l, r in LR:
        if i + l <= n:
            dp[i + l] = (dp[i + l] + s) % mod
            if i + r + 1 <= n:
                dp[i + r + 1] = (dp[i + r + 1] - s) % mod

print(dp[n])
