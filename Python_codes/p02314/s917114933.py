n, m = map(int, input().split())
c = sorted(list(map(int, input().split())))
dp = [[0]*(n+1) for _ in range(m)]

dp[0] = [i  for i in range(n+1)]
for i in range(1, m):
    for j in range(1, n+1):
        if c[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-c[i]]+1)
print(dp[m-1][n])
