from heapq import heapify,heappush,heappop
n = int(input())
INF = float("inf")
adj = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    adj[a].append((b,c))
    adj[b].append((a,c))
H = []
heapify(H)
searched = [0]*n
q,k = map(int,input().split())
k-=1
d = [INF]*n
d[k] = 0
heappush(H, (0,k))
while H:
    f = heappop(H)
    u = f[-1]
    searched[u] = 1
    if d[u] < f[0]:
        continue
    for j in range(len(adj[u])):
        v = adj[u][j][0]
        if searched[v]:
            continue
        if d[v] > d[u]+adj[u][j][-1]:
            d[v] = d[u]+adj[u][j][-1]
            heappush(H,(d[v],v))
for _ in range(q):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    print(d[x]+d[y])