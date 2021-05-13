from collections import deque

# (sx, sy) から (gx, gy) への最短距離を求める
# 辿り着けないと INF
def bfs():
    # すべての点を INF で初期化
    d = [[float("inf")] * m for i in range(n)]

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    #queの定義
    que = deque([])
   
    for i in range(n):
        for j in range(m):
            # スタートとゴールの座標を探す
            if maze[i][j] == "#":
                sx = i
                sy = j
                que.append((sx, sy))
                d[sx][sy] = 0

    # キューが空になるまでループ
    while que:
        # キューの先頭を取り出す
        p = que.popleft()
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を (nx, ny) とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # d[nx][ny] != INF なら訪れたことがある
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                # 移動できるならキューに入れ、その点の距離を p からの距離 +1 で確定する
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, d[i][j])
    
    return ans

n, m = map(int, input().split())
maze = [list(input()) for i in range(n)]

print(bfs())
