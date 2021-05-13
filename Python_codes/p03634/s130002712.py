n = int(input())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    a, b, c = a - 1, b - 1, c
    tree[a].append((b, c))
    tree[b].append((a, c))

from heapq import heappush, heappop
INF = 10 ** 18
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in tree[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

q, k = map(int, input().split())
k -= 1
dist = dijkstra(k, n)
for i in range(q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    res = dist[x] + dist[y]
    print(res)