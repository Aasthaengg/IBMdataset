import heapq as hp
import numpy as np

h, w = map(int, input().split())
s = np.array([list(input()) for _ in range(h)])
s = np.pad(s, 1, 'constant')
visited = np.zeros_like(s, dtype=np.bool)

judge = np.inf

q = []
hp.heappush(q, (0, 1, 1))

while q:
    cnt, y, x = hp.heappop(q)
    if y == h and x == w:
        judge = cnt
        break
    for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ny, nx = y + dy, x + dx
        if s[ny, nx] == '.' and not visited[ny, nx]:
            visited[ny, nx] = True
            hp.heappush(q, (cnt + 1, ny, nx))

if judge == np.inf:
    print(-1)
else:
    print((s == '.').sum() - judge - 1)