import sys
from heapq import heappop, heappush
#import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

def dijkstra(start):
    INF = 10 ** 5
    dist = [INF] * (N+1) # dist[0]は使わない
    dist[start] = 0
    que = [(0, start)]
    while que:
        # (d, v) はdが現在の最小の交通費、vが現在の場所
        d, v = heappop(que)
        # 今より安い交通費で既に来たことがある場合、continue
        if dist[v] < d:
            continue
        for next_city, cost in edges[v].items():
            # modeによって円かスヌークを使うか選ぶ
            d1 = d + cost
            # 次の場所の交通費より安くなる場合は、データを更新
            if dist[next_city] > d1:
                dist[next_city] = d1
                heappush(que, (d1, next_city))
    return dist

N, M = rl()
INF = 10 ** 5
edges = [{} for _ in range(N+1)]
for _ in range(M):
    a, b, c = rl()
    edges[a][b] = c
    edges[b][a] = c

answer = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if j not in edges[i]:
            continue
        A = dijkstra(i)
        if A[j] < edges[i][j]:
            answer += 1
            edges[i].pop(j)
            edges[j].pop(i)

print(answer)
# 00
