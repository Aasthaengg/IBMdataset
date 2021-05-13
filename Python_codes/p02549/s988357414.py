n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
mod = 998244353

dp = [0] * (n + 1)
dp[1] = 1
sm = 0
for i in range(2, n + 1):
    for l, r in lr:
        if i - r - 1 >= 1:
            sm -= dp[i-r-1]
        if i - l >= 1:
            sm += dp[i-l]

        sm %= mod

    dp[i] = sm

ans = dp[n]
print(ans)
