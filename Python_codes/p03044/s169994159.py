import sys
sys.setrecursionlimit(10**8)
N = int(input())
UVW = [tuple(map(int,input().split())) for i in range(N-1)]
es = [[] for _ in range(N)]
for u,v,w in UVW:
    u,v = u-1,v-1
    es[u].append((v,w))
    es[v].append((u,w))

ans = [None] * N
ans[0] = 0

def dfs(v,p=-1):
    for to,d in es[v]:
        if to==p: continue
        ans[to] = ans[v] ^ (d%2)
        dfs(to,v)
dfs(0)

print(*ans, sep='\n')