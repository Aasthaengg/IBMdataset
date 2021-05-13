N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = A
cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if all(dp[i][j] < dp[i][k] + dp[k][j] for k in range(N) if k != i and k != j):
            cnt += dp[i][j]
        if any(dp[i][j] > dp[i][k] + dp[k][j] for k in range(N)):
            print(-1)
            exit()

print(cnt)
