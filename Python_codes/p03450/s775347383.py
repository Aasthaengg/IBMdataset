# -*- coding: utf-8 -*-
from collections import deque
N, M = map(int, input().split(' '))
graph = [[] for _ in range(N)]
for i in range(M):
    l, r, d = map(int, input().split(' '))
    l -= 1
    r -= 1
    graph[l].append((r, d))
    graph[r].append((l, -d))

dsts = [float('inf') for _ in range(N)]

for n in range(N):
    if dsts[n] != float('inf'):
        continue

    buf = deque()
    buf.append(n)
    dsts[n] = 0
    while buf:
        src = buf.popleft()
        for dst, d, in graph[src]:
            next_d = dsts[src] + d

            if dsts[dst] == float('inf'):
                dsts[dst] = next_d
                buf.append(dst)

            elif dsts[dst]  != next_d:
                # print(dsts)
                # print(dst, src, dsts[dst], dsts[src], d, next_d)
                print("No")
                exit()

print("Yes")


