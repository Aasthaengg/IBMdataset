N, M = [int(x) for x in input().split()]
A = [int(input()) for _ in range(M)]

aset = set(A)
MOD = 10 ** 9 + 7

dp = [0] * (N + 1)

if 1 not in aset:
    dp[1] = 1

if 2 not in aset and N >= 2:
    dp[2] += dp[1] + 1

for i in range(3, N + 1):
    if i in aset:
        continue

    dp[i] += dp[i - 1]
    dp[i] += dp[i - 2]

print(dp[N] % MOD)
