from collections import deque
h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

gidx = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            grid[i][j] = gidx
            gidx += 1
node_cnt = gidx
g = [[] for _ in range(node_cnt)]
for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            gidx = grid[i][j]
            #上下左右
            if i > 0 and grid[i-1][j] != '#':
                g[gidx].append(grid[i-1][j])
            if i < h-1 and grid[i+1][j] != '#':
                g[gidx].append(grid[i+1][j])
            if j > 0 and grid[i][j-1] != '#':
                g[gidx].append(grid[i][j-1])
            if j < w-1 and grid[i][j+1] != '#':
                g[gidx].append(grid[i][j+1])

num_white = sum(s.count('.') for s in g)
d = [-1] * node_cnt
seen = [False] * node_cnt

q = deque()
def bfs():
    q.append(0)
    d[0] = 0
    seen[0] = True
    while len(q) > 0:
        now_v = q.popleft()
        for new_v in g[now_v]:
            if seen[new_v]:
                continue
            seen[new_v] = True
            q.append(new_v)
            d[new_v] = d[now_v] + 1

bfs()
ok = True
if grid[0][0] == '#' or grid[h-1][w-1] == '#' or d[node_cnt - 1] == -1:
    ok = False

print(node_cnt - d[node_cnt - 1] - 1 if ok else -1)