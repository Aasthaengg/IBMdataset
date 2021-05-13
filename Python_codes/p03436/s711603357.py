from collections import deque


def bfs(sy, sx, gy, gx):
    q = deque([[sy, sx]])
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ny, nx = y+j, x+k
            if ny < 0 or ny > h-1 or nx < 0 or nx > w-1 or path[ny][nx] == "#":
                continue
            if path[ny][nx] == "." and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x]+1
                q.append([ny, nx])


h, w = map(int, input().split())
path = [input() for _ in range(h)]
visited = [[-1]*w for _ in range(h)]
sy, sx = 0, 0
gy, gx = h-1, w-1
bfs(sy, sx, gy, gx)

count = 0
for i in range(h):
    for j in range(w):
        if path[i][j] == '#':
            count += 1
if visited[gy][gx] != -1:
    print(h*w-count-(visited[gy][gx]+1))
else:
    print(-1)
