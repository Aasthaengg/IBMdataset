n, m = map(int, input().split())
c = list(map(int, input().split())) #0-index

# dp[i+1][x]:i種類のコインを使ってxを支払う際の最小のコイン枚数
dp = [[float('inf')]*(n+1) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    for x in range(n+1):
        dp[i+1][x] = dp[i][x]

        if x -c[i]>= 0:
            dp[i+1][x] = min(dp[i+1][x - c[i]] + 1, dp[i][x])
print(dp[m][n])
