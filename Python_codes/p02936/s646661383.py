import sys
sys.setrecursionlimit(10**6)
n, q = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

c = [0] * n

for j in range(q):
    p, x = map(int, input().split())
    c[p - 1] += x

used = [0] * n
used[0] = 1

def dfs(x):
    cost=c[x]
    for nx in g[x]:
        if used[nx]:
            continue
        used[nx]=1
        c[nx]+=cost
        dfs(nx)
dfs(0)
print(*c)