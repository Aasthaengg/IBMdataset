#!/usr/bin/env python3
from collections import deque

n, m = map(int, input().split())
graph = [deque([]) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph[1]:
    if n in graph[i]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
