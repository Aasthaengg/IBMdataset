import copy
from collections import deque

h, w = map(int, input().split())
grid = [list(map(lambda x: x == "#", input().rstrip())) for _ in range(h)]

q = deque([])
for i in range(h):
    for j in range(w):
        if grid[i][j]:
            q.append([i, j, 0])

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

ans = 0
while q:
    curr = q.popleft()
    ans = max(ans, curr[2])
    for m in moves:
        nx, ny = curr[0] + m[0], curr[1] + m[1]
        if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1 or grid[nx][ny]:
            continue
        else:
            q.append([nx, ny, curr[2] + 1])
            grid[nx][ny] = True

print(ans)