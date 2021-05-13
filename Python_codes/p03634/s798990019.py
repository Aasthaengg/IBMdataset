N = int(input())
abc = [list(map(int, input().split())) for _ in range(N - 1)]

Q, K = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(Q)]

graph = [[] for _ in range(N)]
for i, (ai, bi, ci) in enumerate(abc):
    graph[ai - 1].append((bi - 1, ci))
    graph[bi - 1].append((ai - 1, ci))

import heapq
MY_INF = None
    
q = [(0, K - 1)]
d = [MY_INF] * N
d[K - 1] = 0
while len(q) > 0:
    dist, src = heapq.heappop(q)
    for dst, c_dst in graph[src]:
        dist_tmp = dist + c_dst
        if d[dst] == None or d[dst] > dist_tmp:
            d[dst] = dist_tmp
            heapq.heappush(q, (dist_tmp, dst))

for i, (xi, yi) in enumerate(xy):
    print(d[xi - 1] + d[yi - 1])