h, w = map(int, input().split())
A = [[] for _ in range(h)]
for i in range(h):
    A[i] = list(input())

from collections import deque

visited = [[False] * w for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(w):
        if A[i][j] == '#':
            q.append((i, j, 0))
            visited[i][j] = True

cnt = 0
while q:
    y, x, count = q.popleft()
    cnt = max(cnt, count)
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= h or nx < 0 or nx >= w: continue
        if visited[ny][nx]: continue
        q.append((ny, nx, count + 1))
        visited[ny][nx] = True
print(cnt)