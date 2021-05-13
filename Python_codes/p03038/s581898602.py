import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())

import heapq
q = []
a = map(int, readline().split())
for i in a:
    heapq.heappush(q, (-i, 1))
for i in range(m):
    b, c = map(int, readline().split())
    heapq.heappush(q, (-c, b))

ans = 0
for i in range(n):
    p = heapq.heappop(q)
    ans += abs(p[0])
    if p[1] > 1:
        heapq.heappush(q, (p[0], p[1] - 1))

print(ans)