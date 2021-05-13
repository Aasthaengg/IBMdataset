import sys
input = sys.stdin.buffer.readline

R, C, K = map(int,input().split())
RC = [[0] * (C+1) for _ in range(R+1)]

for _ in range(K):
    r, c, v = map(int,input().split())
    RC[r-1][c-1] = v


dp = [[[0] * (C+1) for i in range(R+1)] for j in range(4)]

dp[1][0][0] = RC[0][0]
for r in range(R):
    for c in range(C):
        for i in range(4):
            dp[i][r][c+1] = max(dp[i][r][c], dp[i][r][c+1])
            if i <= 2:
                dp[i+1][r][c+1] = max(dp[i][r][c] + RC[r][c+1], dp[i+1][r][c+1])
            dp[0][r+1][c] = max(dp[i][r][c], dp[0][r+1][c])
        dp[1][r+1][c] = max(dp[1][r+1][c], dp[0][r+1][c] + RC[r+1][c])

print(max(dp[0][-2][-2], dp[1][-2][-2], dp[2][-2][-2], dp[3][-2][-2]))
