import sys
import math
import itertools
import collections
import heapq
import numpy as np

rl = sys.stdin.readline

n, m = map(int, rl().split())
h = list(map(lambda x: -1*int(x), rl().split()))
heapq.heapify(h)
for _ in range(m):
    heapq.heappushpop(h, math.ceil(h[0]/2))
print(-sum(h))