#!/usr/bin/env python3
import sys
import collections

sys.setrecursionlimit(10 ** 7)

# 1 ✕ 1 (int)
N = int(input().rstrip())

# N ✕ M (2D array)
A = list(map(int, input().rstrip().split()) for _ in range(N - 1))

items = [[] for _ in range(N)]
colors = [-1 for _ in range(N)]

for i in range(N - 1):
    a, b, w = A[i]
    items[a - 1].append((b - 1, w))
    items[b - 1].append((a - 1, w))

queue = collections.deque()
queue.append(0)
colors[0] = 0
while queue:
    v = queue.popleft()
    c = colors[v]
    for k, w in items[v]:
        cc = colors[k]
        if cc == -1:
            nc = c if w % 2 == 0 else not c
            colors[k] = nc
            queue.append(k)

# def dfs(v, c):
#     colors[v] = c
#
#     cc = colors[k]
#
#     if cc == -1:
#         if not dfs(k, nc):
#             return False
#     else:
#         if colors[i] != nc:
#             return False
#
#
# return True
#
# dfs(0, True)
for c in colors:
    print(int(not c))
