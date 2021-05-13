import sys

#O(ElogV)
import heapq
def dijkstra_heap(s, n, edges):
    # 始点sから各頂点への最短距離
    dist = [float("inf")] * n
    used = [True] * n # True:未確定
    dist[s] = 0
    used[s] = False
    used_edges = set()
    edgelist = []
    for (d, e) in edges[s]:
        # 利用した辺を管理するため、sも入れていることに注意
        heapq.heappush(edgelist, (d, e, s))
    while edgelist:
        d, e, s = heapq.heappop(edgelist)
        if dist[e] >= d:
            if s < e:
                used_edges.add((s, e))
            else:
                used_edges.add((e, s))

        # まだ使われてない頂点の中から最小の距離のものを探す
        if not used[e]:
            continue
        dist[e] = d
        used[e] = False

        """
        if s < e:
            used_edges.add((s, e))
        else:
            used_edges.add((e, s))
        """
        for (nd, ne) in edges[e]:
            if used[ne]:
                heapq.heappush(edgelist, (nd + dist[e], ne, e))
    return dist, used_edges

N, M = map(int, sys.stdin.readline().strip().split())

edges = [[] for _ in range(N)]
all_edges = set()
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    edges[a-1].append((c, b-1))
    edges[b-1].append((c, a-1))
    if a < b:
        all_edges.add((a-1, b-1))
    else:
        all_edges.add((b-1, a-1))

for i in range(N):
    min_d, used_edges = dijkstra_heap(i, N, edges)
    # 利用した辺を取り除く
    all_edges -= used_edges

print(len(all_edges))