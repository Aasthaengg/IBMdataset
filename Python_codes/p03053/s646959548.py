from collections import deque

h, w = map(int, input().split())
grid = [input() for i in range(h)]

dist = [[-1]*w for i in range(h)]

black = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            black.append((i, j))
            dist[i][j] = 0

def bfs(black, dist):
    d = 0
    while black:
        x, y = black.popleft()
        d = dist[x][y]
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not(0 <= nx < h) or not(0 <= ny < w):
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = d+1
                black.append((nx, ny))
    return d

d = bfs(black, dist)
print(d)