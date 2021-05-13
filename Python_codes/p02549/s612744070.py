N, K = map(int, input().split())
L = []
R = []
for i in range(K):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
mod = 998244353

dp = [0] * (N + 1)
dpsum = [0] * (N + 1)
"""
dp[i] : iまでの個数
dpsum[i] : iまでのdpの累積和
"""
dp[1] = 1
dpsum[1] = 1
for i in range(2, N + 1):
    for k in range(K):
        r = i - L[k]
        l = i - R[k]
        if r < 0:
            continue
        l = max(1, l)
        dp[i] += (dpsum[r] - dpsum[l - 1]) % mod
    dpsum[i] = (dpsum[i - 1] + dp[i]) % mod

print(dp[N] % mod)

