


import heapq

N = int(input())
es = [[] for _ in range(N)]
for i in range(N-1):
    a,b,c = map(int, input().split())
    es[a-1].append((c, b-1))
    es[b-1].append((c, a-1))

Q,K = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(Q)]

INF = float("inf")

dist = [INF] * N
dist[K-1] = 0
q = []
q.append((0,K-1))

while q:
    cost, curr = heapq.heappop(q)
    if cost > dist[curr]:
        continue

    for c, nxt in es[curr]:
        if dist[curr] + c < dist[nxt]:
            dist[nxt] = dist[curr] + c
            heapq.heappush(q, (dist[nxt], nxt))

for x,y in xy:
    print(dist[x-1] + dist[y-1])


