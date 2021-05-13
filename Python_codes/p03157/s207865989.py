from collections import deque
import sys
input = sys.stdin.readline

def C(i, j):
    p = [1, 0]
    q = deque([(i, j, ".")])
    while q:
        x, y, c = q.popleft()
        for u, v in d:
            dx, dy = x + u, y + v
            if 0 <= dx < h and 0 <= dy < w and s[dx][dy] != c and use[dx][dy]:
                use[dx][dy] = False
                p[s[dx][dy] == "#"] += 1
                q.append((dx, dy, s[dx][dy]))
    return p[0]*p[1]


h, w = map(int, input().split())
s = [input() for i in range(h)]
use = [[1] * w for i in range(h)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
for i in range(h):
    for j in range(w):
        if use[i][j] and s[i][j] == ".":
            use[i][j] = False
            ans += C(i, j)
print(ans)
