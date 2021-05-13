import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

H, W = map(int, input().split())
H += 2
W += 2
B = [0] * H
block = 0
for i in range(H):
    if i == 0 or i == H - 1:
        B[i] = '#' * W
    else:
        B[i] = '#' + input() + '#'
        block += B[i].count("#") - 2

start = (1, 1)
goal = (H - 2, W - 2)

import queue
def bfs(start, goal):
    dist = [[-1] * W for _ in range(H)]
    q = queue.Queue()
    sy, sx = start
    dist[sy][sx] = 1
    q.put(start)

    ys = [0, 1, 0, -1]
    xs = [1, 0, -1, 0]

    while not q.empty():
        y, x = q.get()
        if (y, x) == goal:
            return dist[y][x]

        for dy, dx in zip(ys, xs):
            ny, nx = y + dy, x + dx
            if B[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            q.put((ny, nx))
    return -1

res = bfs(start, goal)
if res == -1:
    print(res)
else:
    print((H - 2) * (W - 2) - block - res)