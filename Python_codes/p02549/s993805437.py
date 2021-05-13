N, K = map(int, input().split())
MOD = 998244353

LR = []

for i in range(K):
    l, r = map(int, input().split())
    LR.append([l, r])

dp = [0] * (N + 1)
dp[1] = 1
cumsum = [0, 1]

for i in range(2, N + 1):
    for l, r in LR:
        if i - l >= 1:
            dp[i] += (cumsum[i - l] - cumsum[max(i - r - 1, 0)]) % MOD
    dp[i] = dp[i] % MOD
    cumsum.append(cumsum[-1] + dp[i])

print(dp[-1] % MOD)
