from collections import defaultdict
from itertools import permutations
import heapq

INF = float('inf')
N, M, R = map(int, input().split())
r = list(map(int, input().split()))

Adj_list = defaultdict(set)

for i in range(M):
    a, b, c = map(int, input().split())   
    Adj_list[a-1].add((b-1, c))
    Adj_list[b-1].add((a-1, c))


def dijkstra(x, vertex):
    d = [INF] * x
    d[vertex] = 0
    hq = [(0, vertex)]
    
    while hq:
        u = heapq.heappop(hq)[1]
        for (v, c) in Adj_list[u]:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                heapq.heappush(hq, (d[u]+c, v))

    return d

ans = INF
t_dis = 0

table = {}
for i in r:
    table[i-1] = dijkstra(N, i-1)

for each in permutations(r):
    t_dis = 0
    for i in range(R-1):
        t_dis += table[each[i]-1][each[i+1]-1]

    ans = min(ans, t_dis)

print(ans)