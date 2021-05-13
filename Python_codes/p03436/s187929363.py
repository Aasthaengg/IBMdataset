h, w = map(int, input().split())

#塗れる最大数
#すなわち、（すべての白）ー（最短経路距離）
g = [input() for _ in range(h)]
from collections import *
d = [[-1]*w for _ in range(h)]
d[0][0] = 0

q = deque([(0, 0)])

while q:
    tx, ty = q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = tx + dx, ty + dy
        if 0 <= nx < h and 0 <= ny < w and g[nx][ny] == '.' and d[nx][ny] < 0:
            d[nx][ny] = d[tx][ty] + 1
            q.append((nx, ny))

if d[-1][-1] < 0:
    print(-1)
    exit()
else:
    print(sum([s.count('.') for s in g]) - d[-1][-1] - 1)