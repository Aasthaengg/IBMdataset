from collections import defaultdict
from collections import deque
h, w = list(map(int, input().split()))
s = [list(map(str, list(input()))) for i in range(h)]  # 文字列の二次元配列入力
cnt_sharp = 0
G = defaultdict(lambda: [])
vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            cnt_sharp += 1
        for dy, dx in vec:
            if 0 <= i+dy < h and 0 <= j+dx < w and s[i+dy][j+dx] == '.':
                G[(i+dy, j+dx)].append((i, j))
# G[v]: 頂点vに隣接する頂点list
dist = defaultdict(lambda: -1)
que = deque([(0, 0)])
dist[(0, 0)] = 1
while que:
    v = que.popleft()
    d = dist[v]
    for ww in G[v]:
        if dist[ww] > -1:
            continue
        dist[ww] = d + 1
        que.append(ww)
if dist[(h-1, w-1)] == -1:
    print(-1)
else:
    print(h*w-cnt_sharp-dist[(h-1, w-1)])
