#!/usr/bin/env python3
from collections import defaultdict, deque
N = int(input())
w = defaultdict(int)
edge = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    w[str(a) + "_" + str(b)] = c
    w[str(b) + "_" + str(a)] = c
    edge[a].append(b)
    edge[b].append(a)

Q, K = map(int, input().split())

root = K
done = [True for _ in range(N + 1)]
done[root] = False
d = [0 for _ in range(N + 1)]
q = deque([root])

while q:
    parent = q.pop()
    for child in edge[parent]:
        if done[child]:
            key = str(parent) + "_" + str(child)
            done[child] = False
            d[child] = d[parent] + w[key]
            q.append(child)

for _ in range(Q):
    x, y = map(int, input().split())
    print(d[x] + d[y])