# C - Grid Repainting 2
from collections import deque

H, W = map(int, input().split())
grid = [[''] * W for _ in range(H)]
for i in range(H):
    grid[i] = list(str(input()))

d = deque()
ans = 'Yes'
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            continue
        d.append((i, j))
        grid[i][j] = '.'
        tmp = 1
        while d:
            p, q = d.popleft()
            for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx = p+x
                ny = q+y
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if grid[nx][ny] == '.':
                    continue
                d.append((nx, ny))
                grid[nx][ny] = '.'
                tmp += 1
        if tmp == 1:
            ans = 'No'
            break
    else:
        continue
    break
print(ans)