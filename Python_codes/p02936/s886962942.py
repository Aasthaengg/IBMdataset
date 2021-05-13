import sys
sys.setrecursionlimit(10**6)
n, q = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(lambda x: x-1, map(int, input().split()))
    G[a].append(b)
    G[b].append(a)

ans = [0]*n
for i in range(q):
    p, x = map(int, input().split())
    ans[p-1] += x

def dfs(v, pre=-1):  
    for nx in G[v]:
        if nx==pre:
            continue
        ans[nx] += ans[v]
        dfs(nx,v)
dfs(0)
print(*ans)