import sys
input = sys.stdin.readline
from collections import deque
mod = 10**9 + 7

n, k = [int(x) for x in input().split()]
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

color = [-1]*n
ans = k

def bfs(u):
    global ans
    queue = deque([u])
    color[u] = k
    while queue:
        v = queue.popleft()
        cnt = 0
        if v == 0:
            start = k - 1
        else:
            start = k -2
        for i in g[v]:
            if color[i] < 0:
                color[i] = start - cnt
                cnt += 1
                ans *= color[i]
                ans %= mod
                queue.append(i)

bfs(0)
print(ans)
# print(color)