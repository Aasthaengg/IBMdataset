import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

#dp[i][j]は(i,j)までの経路の数
dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            dp[i][j] = 0
            continue

        if i > 0 and j > 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        elif i > 0:
            dp[i][j] = dp[i - 1][j]
        elif j > 0:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = 1

print(dp[H-1][W-1] % (10**9+7))