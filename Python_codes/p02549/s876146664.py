N, K = map(int, input().split())
MOD = 998244353

L = []
R = []
for i in range(K):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

dp = [0] * (N + 1)
dp[1] = 1
dp_sum = [0] * (N + 1)
dp_sum[1] = 1
for i in range(2, N + 1):
    for j in range(K):
        li = max(i - R[j], 1)
        ri = i - L[j]
        if ri < 1:
            continue
        dp[i] += (dp_sum[ri] - dp_sum[li - 1]) % MOD
    dp_sum[i] = (dp_sum[i - 1] + dp[i]) % MOD

print(dp[-1] % MOD)
