n, ma, mb = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x.insert(0, [0, 0, 0])
inf = 114514
dp = [[[inf] * (10 * n + 1) for _ in range(10 * n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = 0
suma, sumb = 0, 0
for i in range(1, n + 1):
    suma += x[i][0]
    sumb += x[i][1]
    for j in range(suma + 1):
        for k in range(sumb + 1):
            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
            if j >= x[i][0] and k >= x[i][1]:
                dp[i][j][k] = min(dp[i - 1][j][k], dp[i - 1][j - x[i][0]][k - x[i][1]] + x[i][2])
ans = 114514
for i in range(1, 10 * n + 1):
    for j in range(1, 10 * n + 1):
        if i * mb == j * ma:
            ans = min(ans, dp[n][i][j])
print(ans if not ans == 114514 else -1)