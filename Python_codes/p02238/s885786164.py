import sys

n = int(input())
G = [None]*(n+1)
for i in range(n):
    u, k, *vs = map(int, input().split())
    G[u] = vs

d = [-1]*(n+1)
f = [-1]*(n+1)
lb = iter(range(1, 2*n+1)).__next__
def dfs(v):
    d[v] = lb()
    for w in G[v]:
        if d[w] != -1: #already visited
            continue
        dfs(w)
    f[v] = lb()

for v in range(1, n+1):
    if d[v] != -1:
        continue
    dfs(v)

for v in range(1, n+1):
    print(f"{v} {d[v]} {f[v]}")
