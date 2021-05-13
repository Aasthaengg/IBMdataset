h, w = map(int, input().split())
A = [list(str(input())) for _ in range(h)]

from collections import deque
q = deque([])
visit = [[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if A[i][j] == '#':
            q.append((i, j))
            visit[i][j] = 0

while q:
    y, x = q.popleft()
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w:
            if visit[ny][nx] == -1:
                visit[ny][nx] = visit[y][x]+1
                q.append((ny, nx))
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, visit[i][j])
print(ans)
