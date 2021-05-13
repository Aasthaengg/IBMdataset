# Review problem
from collections import deque
H, W = map(int, input().split())
D = [list(input()) for i in range(H)]

visited = [[False for i in range(W)] for j in range(H)]
dis = [[0 for i in range(W)] for j in range(H)]

black = deque()
dif = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(H):
    for j in range(W):
        if D[i][j] == "#":
            visited[i][j] = True
            black.append((i, j))

while black:
    x, y = black.popleft()
    for dx, dy in dif:
        if 0 <= dx+x < H and 0 <= dy+y < W and visited[dx+x][dy+y] == False:
            visited[dx+x][dy+y] = True
            dis[dx+x][dy+y] = dis[x][y]+1
            black.append((dx+x, dy+y))
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, dis[i][j])
print(ans)