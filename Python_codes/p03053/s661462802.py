from collections import deque

h, w = map(int, input().split())
a = [input() for _ in range(h)]

d = deque()
dist = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            d.append([i, j])
            dist[i][j] = 0

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
while d:
    x1, y1 = d.popleft()

    for i in range(4):
        x2 = x1 + dx[i]
        y2 = y1 + dy[i]

        if 0 <= x2 < h and 0 <= y2 < w and dist[x2][y2] == -1:
            d.append([x2, y2])
            dist[x2][y2] = dist[x1][y1] + 1

print(max(list(map(lambda x: max(x), dist))))