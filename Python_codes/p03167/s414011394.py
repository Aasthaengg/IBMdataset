N, M = map(int,input().split())
maze = [input() for _ in range(N)]
dp = [[0]*M for _ in range(N)]
mod = 10**9 + 7

dp[0][0] = 1
for i in range(N):
    for j in range(M):
        if maze[i][j] != "#":
            if i-1 >= 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
            if j-1 >= 0:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod

print(dp[N-1][M-1])