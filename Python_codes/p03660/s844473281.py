import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

import copy

n = ni()
g = [{} for _ in range(n)]

for i in range(n-1):
    a,b = na()
    a,b = a-1,b-1
    g[a][i] = b
    g[b][i] = a

dis = [float('inf')]*n
near = [-1]*n
gg = [copy.deepcopy(line) for line in g]

def dfs(v,start,depth):
    if dis[v] > depth:
        dis[v] = depth
        near[v] = start
    if not g[v]:
        return
    while g[v]:
        key,nv = g[v].popitem()
        g[nv].pop(key)
        dfs(nv,start,depth+1)

dfs(0,0,0)
g = gg
dfs(n-1,n-1,0)

print('Fennec' if 2*near.count(0) > n else 'Snuke')
