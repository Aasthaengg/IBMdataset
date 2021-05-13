n = int(input())
p = [float(i) for i in input().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i, j in enumerate(p):
    for k in range(n):
        dp[i + 1][k + 1] += dp[i][k] * j
        dp[i + 1][k] += dp[i][k] * (1 - j)
ans = 0
for i in range(n + 1):
    if i > (n - i):
        ans += dp[-1][i]
print(ans)
