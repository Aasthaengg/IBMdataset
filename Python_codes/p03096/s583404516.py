n = int(input())
C = []
MOD = 10 ** 9 + 7
pre = -1
for i in range(n):
    a = int(input())
    if a != pre:
        C.append(a)
    pre = a

N = len(C)
dp = [0] * (N + 1)
col = {}
pre = -1
dp[0] = 1
for i in range(1, N + 1):
    if C[i - 1] not in col:
        dp[i] = dp[i - 1]
        col[C[i - 1]] = dp[i]
    else:
        dp[i] = dp[i - 1]
        dp[i] += col[C[i - 1]]
        dp[i] %= MOD
        col[C[i - 1]] += dp[i - 1]

print(dp[N])
