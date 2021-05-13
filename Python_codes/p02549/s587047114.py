N, K = map(int, input().split())

L, R = [], []

for _ in range(K):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

dp = [0] * 300000
dpsum = [0] * 300000
dp[1] = 1
dpsum[1] = 1

for i in range(2, N+1):
    for j in range(K):
        li = min(L[j], i)
        ri = min(R[j], i + 1)
        dp[i] += dpsum[i - li] - dpsum[i - ri - 1]

    dp[i] %= 998244353
    dpsum[i] = dpsum[i-1] + dp[i]

print(dp[N])