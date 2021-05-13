N, K = map(int, input().split())
mod = 998244353

LR = [tuple(map(int, input().split())) for _ in range(K)]
LR.sort()

dpsum = [0] * (N + 1)
dpsum[1] = 1
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    for L, R in LR:
        l = i - R
        r = i - L
        
        if r < 0:
            continue
        l = max(l, 0)
        
        dp[i] += dpsum[r] - dpsum[l - 1]
        dp[i] %= mod
    dpsum[i] = dpsum[i - 1] + dp[i]

print(dp[N])
