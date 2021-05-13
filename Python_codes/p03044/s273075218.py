# -*- coding: utf-8 -*-
import math
N = int(input())
graph = [{} for _ in range(N)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = w
    graph[v][u] = w

d = [-1 for _ in range(N)]
src = 0
d[src] = 0
buf = [src]

while buf:
    src = buf.pop()
    for dst, w in graph[src].items():
        if d[dst] == -1:
            d[dst] = d[src] + w
            buf.append(dst)

for n in d:
    if n % 2:
        print(0)
    else:
        print(1)