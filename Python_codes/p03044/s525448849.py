import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())
ver = [[] for i in range(N+1)]
for i in range(N-1):
    u,v,w = map(int,readline().split())
    ver[u].append((v,w))
    ver[v].append((u,w))
color = [-1]*(N+1)
color[1] = 0
def dfs(fro,to,d):
    color[to] = d%2
    for v in ver[to]:
        if v[0] == fro:
            continue
        dfs(to,v[0],d+v[1])


for v in ver[1]:
    dfs(1,v[0],v[1])

for i in range(1,N+1):
    print(color[i])
