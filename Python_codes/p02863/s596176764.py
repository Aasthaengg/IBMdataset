N, T = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort()

ans = 0
dp = [[0 for _ in range(3005)] for _ in range(3005)]
for i in range(N):
    a, b = AB[i]
    for j in range(T):
        # iを使わないパターン
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # iを使うパターン
        nj = j + a
        if nj < T:
            dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j] + b)
    now = dp[i][T - 1] + b
    ans = max(ans, now)

print(ans)
