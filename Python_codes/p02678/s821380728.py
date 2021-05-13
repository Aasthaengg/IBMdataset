#!/usr/bin/env python3
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

que = deque()
dist = [float('inf')] * n
prev = [-1] * n
dist[0] = 0
que.append(0)
while que:
    now = que.popleft()
    for edge in edges[now]:
        if dist[edge] > dist[now] + 1:
            dist[edge] = dist[now] + 1
            prev[edge] = now + 1
            que.append(edge)


print('Yes')
for i in range(1, n):
    print(prev[i])

