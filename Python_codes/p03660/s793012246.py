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

dist = [(0,-1) for _ in range(n)]
def dfs(now,prev=-1):
    for nxt in G[now]:
        if nxt == prev: continue
        dist[nxt] = (dist[now][0]+1,now)
        dfs(nxt,now)
dfs(0)

color = ["?"]*n
cnt = 0
now = n-1
w = (dist[n-1][0]+1)//2
while now != -1:
    if cnt < w: color[now] = -1
    else: color[now] = 1
    cnt += 1
    now = dist[now][1]

def coloring(now,prev=-1):
    for nxt in G[now]:
        if nxt == prev: continue
        if color[nxt] != "?" and color[now] != color[nxt]: continue
        color[nxt] = color[now]
        coloring(nxt,now)
coloring(0)
coloring(n-1)

print("Fennec" if sum(color) > 0 else "Snuke")