MOD = 10 ** 9 + 7
n = int(input())
c = [int(input()) for _ in range(n)]
l = [c[0]]
for i in range(1, n):
    if c[i] != c[i - 1]:
        l.append(c[i])
n = len(l)
p = [-1] * (max(c) + 1)
q = [-1] * n
for i, x in enumerate(l[::-1]):
    q[n - i - 1] = p[x]
    p[x] = n - i - 1
dp = [0] * (n + 1)
dp[0] = 1
for i in range(n):
    dp[i + 1] += dp[i]
    if q[i] != -1:
        dp[q[i] + 1] += dp[i + 1]
print(dp[n] % MOD)
