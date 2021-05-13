H, W = map(int, input().split())
gridgraph = [input() for _ in range(H)]

dp = [[10000]*W for _ in range(H)]

if gridgraph[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

adjacent = [[1, 0], [0, 1]]

for i in range(H):
    for j in range(W):
        for dy, dx in adjacent:
            ny = i+dy
            nx = j+dx
            if ny == H or nx == W:
                continue
            # 壁の中に移動する時
            if gridgraph[i][j] == "." and gridgraph[ny][nx] == "#":
                dp[ny][nx] = min(dp[i][j]+1, dp[ny][nx])
            else:
                dp[ny][nx] = min(dp[i][j], dp[ny][nx])
print(dp[H-1][W-1])
