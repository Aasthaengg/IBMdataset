INF = 10 ** 10
n, m = map(int, input().split())
dp = [[INF] * (2 ** n) for _ in range(m + 1)]
a = [0] * m
c = [0] * m
for i in range(m):
    a[i], b = map(int, input().split())
    t = 0
    for k in list(map(int, input().split())):
        t += 1 << (k - 1)
    c[i] = t
dp[0][0] = 0
for i in range(m):
    for j in range(2 ** n):
        dp[i + 1][j | c[i]] = min(dp[i + 1][j | c[i]], dp[i][j] + a[i])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
ans = dp[m][(1 << n) - 1]
if ans == INF:
    print(-1)
else:
    print(ans)
