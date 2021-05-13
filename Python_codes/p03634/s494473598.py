import sys
sys.setrecursionlimit(100000000)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b,c))
    G[b].append((a,c))
q,k = map(int,input().split())
k -= 1

dist = [-1]*n
dist[k] = 0
def dfs(now):
    for nxt,d in G[now]:
        if dist[nxt] != -1: continue
        dist[nxt] = dist[now] + d
        dfs(nxt)
dfs(k)

ans = [0]*q
for i in range(q):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    ans[i] = dist[x]+dist[y]

for i in range(q): print(ans[i])