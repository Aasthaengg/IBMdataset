# -*- coding:utf-8 -*-

def solve():
    import sys
    import heapq

    N = int(sys.stdin.readline())
    graph = []
    for _ in range(N):
        _in = list(map(int, sys.stdin.readline().split()))
        if len(_in) == 2:
            graph.append([])
            continue
        u, k, Vs = _in[0], _in[1], _in[2:]
        As = []
        for v in Vs:
            As.append(v-1)
        graph.append(As)

    dist = [float("inf") for _ in range(N)]
    dist[0] = 0
    que = []
    heapq.heappush(que, (0, 0))  # (頂点番号, 最短距離の候補)
    while que:
        u, d = heapq.heappop(que)
        if dist[u] < d: continue

        for v in graph[u]:
            if dist[v] > dist[u]+1:
                dist[v] = dist[u]+1
                heapq.heappush(que, (v, dist[v]))

    for i in range(N):
        d = -1 if dist[i]==float("inf") else dist[i]
        print(i+1, d)


if __name__ == "__main__":
    solve()

