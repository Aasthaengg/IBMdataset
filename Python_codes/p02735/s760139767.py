#!/usr/bin/env python3
from queue import Queue

INF = 10 ** 9
dx = [1, 0]
dy = [0, 1]

h, w = map(int, input().split())
s = [input() for _ in range(h)]
dist = [[INF] * w for _ in range(h)]
dist[0][0] = 0

q = Queue()
sx, sy = 0, 0
q.put([0, 0])
while not q.empty():
    ux, uy = q.get()
    for k in range(2):
        vx = ux + dx[k]
        vy = uy + dy[k]
        if not (0 <= vx < h and 0 <= vy < w):
            continue
        cost = s[ux][uy] == "#" and s[vx][vy] == "."
        if dist[vx][vy] > dist[ux][uy] + cost:
            dist[vx][vy] = dist[ux][uy] + cost
            q.put([vx, vy])

print(dist[-1][-1] + (s[-1][-1] == "#"))
