#!/usr/bin/env python3
from collections import deque

n, q = map(int, input().split())

graph = [deque([]) for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

a = [0] * -~n
b = [True] * -~n
for i in range(q):
    p, x = map(int, input().split())
    a[p] += x

d = deque([1])

while len(d):
    p = d.popleft()
    for i in graph[p]:
        if b[i]:
            a[i] += a[p]
            d.append(i)
            graph[i].remove(p)
print(*a[1:])
