import heapq

n,m = map(int,input().split())
abc = [list(map(int,input().split())) for _ in range(m)]

edges = [[] for _ in range(n)]
for a,b,dis in abc:
    edges[a-1].append((b-1, dis))
    edges[b-1].append((a-1, dis))

def dijkstra(edges, s):
    hq = []
    d = [-1] * n
    d[s] = 0
    heapq.heappush(hq, (0, s))
    while hq:
        d1, p = heapq.heappop(hq)
        for p2, d2 in edges[p]:
            if d[p2] == -1 or d[p2] > d1 + d2:
                d[p2] = d1 + d2
                heapq.heappush(hq, (d1+d2, p2))
    return d

d = []

for i in range(n):
    d.append(dijkstra(edges, i))

ans = 0

for a,b,dis in abc:
    if dis > d[a-1][b-1]:
        ans += 1

print(ans)
