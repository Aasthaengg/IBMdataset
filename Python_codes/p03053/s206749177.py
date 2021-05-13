from collections import deque

h, w = map(int, input().split())
a = [input() for _ in range(h)]
que = deque([])
dst = [[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            que.append([i, j])
            dst[i][j] = 0

max_d = 0
while que:
    y, x = que.popleft()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if a[ny][nx] == '#':
            continue
        if dst[ny][nx] != -1:
            continue

        dst[ny][nx] = dst[y][x] + 1
        max_d = dst[y][x] + 1
        que.append([ny, nx])
print(max_d)
