from heapq import heappop,heappush

def dijkstra(G, start):
    n = len(G)
    dist = [float("inf")]*n
    visited = set()
    heap = []
    heap.append((0, start))

    while heap and len(visited) != n:
        d, cur = heappop(heap)
        if cur in visited:
            continue
        visited.add(cur)
        dist[cur] = d
        for to in range(10):
            if to not in visited:
                heappush(heap, (d+G[cur][to], to))
    return dist

h,w = map(int, input().split())
c = [list(map(int, input().split())) for i in range(10)]
rc = [[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        rc[i][j] = c[j][i]
a = [list(map(int, input().split())) for i in range(h)]
dist = dijkstra(rc, 1)
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += dist[a[i][j]]
print(ans)