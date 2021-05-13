import sys
sys.setrecursionlimit(1000000000)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist1 = [-1]*n
dist1[0] = 0
dist2 = [-1]*n
dist2[n-1] = 0
def dfs(now,dist):
    for nxt in G[now]:
        if dist[nxt] != -1: continue
        dist[nxt] = dist[now]+1
        dfs(nxt,dist)
dfs(0,dist1)
dfs(n-1,dist2)

fennec = snuke = 0
for i in range(n):
    if dist1[i] <= dist2[i]: fennec += 1
    else: snuke += 1
print("Fennec" if fennec > snuke else "Snuke")