import sys
def input(): return sys.stdin.readline().rstrip()

R, C, k = (int(x) for x in input().split())
V = [[0] * (C + 5) for _ in range(R + 5)]
for _ in range(k):
    r, c, v = (int(x) for x in input().split())
    V[r][c] = v

# dp[3][i][j]
dp = [[[0] * (C + 5) for _ in range(R + 5)] for _ in range(4)]
for i in range(R + 3):
    for j in range(C + 3):
        for k in range(4):
            # 行移動
            dp[0][i + 1][j] = max(dp[0][i + 1][j], dp[k][i][j])
            dp[1][i + 1][j] = max(dp[1][i + 1][j], dp[k][i][j] + V[i + 1][j])
            # 列移動
            dp[k][i][j + 1] = max(dp[k][i][j + 1], dp[k][i][j])
            if k < 3:
                dp[k + 1][i][j + 1] = max(dp[k + 1][i][j + 1], dp[k][i][j] + V[i][j + 1])
print(max(dp[k][R][C] for k in range(4)))
