R, C, K = map(int, input().split())
T = [[0]*(C+2) for _ in range(R+2)]
dp = [[[0]*(C+2) for _ in range(R+2)] for _ in range(4)]
for i in range(K):
    r, c, v = map(int, input().split())
    T[r][c] = v
dp[1][1][1] = T[1][1]
dp[0][1][1] = 0

for i in range(1, R+1):
    for j in range(1, C+1):
        for k in range(4):
            dp[0][i+1][j] = max(dp[0][i+1][j], dp[k][i][j])
            dp[1][i+1][j] = max(dp[1][i+1][j], dp[k][i][j] + T[i+1][j])
            dp[k][i][j+1] = max(dp[k][i][j+1], dp[k][i][j])
            if k <= 2:
                dp[k+1][i][j+1] = max(dp[k+1][i][j+1], dp[k][i][j] + T[i][j+1])
ans = 0
for k in range(4):
    ans = max(ans, dp[k][R][C])
print(ans)