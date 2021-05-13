# H - Grid 1
H,W = map(int,input().split())
maze = []
for _ in range(H):
    a = list(input())
    maze.append(a)

# dp[i][j]: 座標 (i, j) に到達できる経路の数
dp = [[0]*(W) for _ in range(H)]

# 初期条件 
# 座標 (0, 0) への経路は 1 通り
dp[0][0] = 1

for h in range(H):
    for w in range(W):
        # スタート位置のときはスルー
        if (h,w) == (0,0):
            continue
        # 壁があるときはスルー
        if maze[h][w] == '#':
            continue
        # 左にマスがあるとき 
        if w > 0:
            dp[h][w] = (dp[h][w] + dp[h][w-1])%(10**9+7)
        # 上にマスがあるとき
        if h > 0:
            dp[h][w] = (dp[h][w] + dp[h-1][w])%(10**9+7)
print(dp[H-1][W-1])