import sys
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = [int(x) for x in input().split()]
    g[a - 1].append([c, b - 1])
    g[b - 1].append([c, a - 1])
q, k = [int(x) for x in input().split()]
import heapq
def dijkstra(s):
    # 始点sから各頂点への最短距離
    d = [float('inf')]*n
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False]*n
    used[s] = True
    # 仮の距離を記録するヒープ
    que = []
    for e in g[s]:
        heapq.heappush(que, e)
    while que:
        minedge = heapq.heappop(que)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in g[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d
d = dijkstra(k - 1)
for _ in range(q):
    x, y = [int(x) for x in input().split()]
    print(d[x - 1] + d[y - 1])
