import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())

nodes = [{} for i in range(N+1)]

for i in range(N-1):
    u,v,w = map(int,readline().split())
    nodes[u][v] = w
    nodes[v][u] = w

ans = [-1]*(N+1)
ans[1] = 0

def dfs(start,to,dist):
    ver = nodes[start][to]
    ans[to] = (dist + ver)%2
    for k in nodes[to].keys():
        if k != start:
            dfs(to,k,dist+ver)

for k in nodes[1].keys():
    dfs(1,k,0)

for i in range(N):
    print(ans[i+1])
