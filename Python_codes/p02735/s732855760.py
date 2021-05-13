H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]
INF = float('inf')
dp = [[INF] * W for _ in range(H)]
if board[0][0] == '.':
    dp[0][0] = 0
else:
    dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if board[i][j] == board[i-1][j]:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        else:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        if board[i][j] == board[i][j-1]:
            dp[i][j] = min(dp[i][j], dp[i][j-1])
        else:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
if board[H-1][W-1] == '#':
    dp[H-1][W-1] += 1
print(dp[H-1][W-1] // 2)

