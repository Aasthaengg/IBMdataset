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

N, M = map(int, readline().split())
A = map(int, readline().split())

import heapq
q = []
for a in A:
    heapq.heappush(q, -a)

while M > 0:
    a = -heapq.heappop(q)
    a //= 2
    heapq.heappush(q, -a)
    M -= 1

ans = 0
while len(q) > 0:
    ans += abs(heapq.heappop(q))
print(ans)
