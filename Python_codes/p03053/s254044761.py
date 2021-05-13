from collections import deque

INF = float('inf')

H,W=map(int,input().split())
grid = [input() for i in range(H)]

# 初期の黒('#')の位置からの距離
dist = [[-1]*W for _ in range(H)]

## '#'の位置をキューに追加（＝今回はこれが複数あるので、複数スタートとなる）
black_cells = deque()
for i in range(H):
    for j in range(W):
        if grid[i][j]=="#":
            dist[i][j]=0
            black_cells.append((i,j))

while black_cells:
    y,x=black_cells.popleft()#黒マスのスタート地点
    d=dist[y][x]#スタート地点からの距離
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        new_x=x+dx
        new_y=y+dy
        if new_y < 0 or H <= new_y or new_x < 0 or W <= new_x:#範囲からはみ出すとき
            continue
        if dist[new_y][new_x]==-1:
            dist[new_y][new_x]=d+1
            black_cells.append((new_y,new_x))
print(d)
