import sys
input = sys.stdin.readline
from collections import deque
mod = 10**9 + 7

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    g[u - 1].append(v - 1)

s, t = [int(x) for x in input().split()]

d = [[-1, -1, -1] for _ in range(n)]

def bfs(u):
    queue = deque([[u, 0]])
    d[u][0] = 0
    while queue:
        v, d_ = queue.popleft()
        for i in g[v]:
            if d[i][(d_ + 1) % 3] < 0:
                d[i][(d_ + 1) % 3] = d_ + 1
                queue.append([i, d_ + 1])
    return d

d = bfs(s - 1)

print(d[t - 1][0] // 3)
