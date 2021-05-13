from collections import defaultdict
N = int(input())
C = [int(input()) for i in range(N)]
MOD = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1

D = defaultdict(int)
for i, c in enumerate(C, start=1):
    dp[i] += dp[i - 1]
    if D[c] > 0 and D[c] != i - 1:
        dp[i] += dp[D[c]]
    dp[i] %= MOD
    D[c] = i

print(dp[-1] % MOD)
