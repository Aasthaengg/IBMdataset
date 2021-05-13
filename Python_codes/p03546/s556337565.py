# dijkstraで解く
from heapq import heappush, heappop
from collections import defaultdict
INF = float("inf")

def dijkstra(C, g):
    '''
    各頂点からg「まで」の最小コストを求める
    C ... 隣接行列で表されたコスト
    g ... 終点
    '''
    n = len(C)
    min_cost = [INF] * n
    min_cost[g] = 0
    visited = defaultdict(bool)
    H = [(0, g)]

    while H:
        v_cost, v = heappop(H)
        if visited[v]: continue
        visited[v] = True
        for u in range(n):
            new_cost = C[u][v] + v_cost
            if new_cost < min_cost[u]:
                min_cost[u] = new_cost
                heappush(H, (new_cost, u))

    return min_cost


H, W = [int(x) for x in input().split()]
C = [[int(x) for x in input().split()] for _ in range(10)]
A = [[int(x) for x in input().split()] for _ in range(H)]

min_cost = dijkstra(C, 1)

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1: continue
        ans += min_cost[A[i][j]]

print(ans)