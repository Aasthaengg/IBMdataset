h, w = map(int, input().split())
a = [list(input()) for _ in range(h)] # #.のグリッドの場合
#print(a)

from collections import deque
step = [(0,1), (0,-1), (1,0), (-1,0)]
que = deque()

seen = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            que.append((i, j))
            seen[i][j] = 0
ans = 0
#import numpy as np
#print(np.array(seen))
while len(que) > 0:
    x, y = que.popleft()
    for tx, ty in step:
        xi, yi = x + tx, y + ty
        if xi < 0 or yi < 0 or xi >= h or yi >= w:
            continue
        if a[xi][yi] == '#':
            continue
        if a[xi][yi] == '.':
            seen[xi][yi] = seen[x][y] + 1
            ans = max(ans, seen[xi][yi])
            a[xi][yi] = '#'
            que.append((xi, yi))
    #print(np.array(seen))
print(ans)


