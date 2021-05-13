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

N, K = map(int, readline().split())
V = list(map(int, readline().split()))

MAX = min(N, K) + 1

ans = 0
for a in range(MAX):
    for b in range(MAX):
        if a + b >= MAX:
            continue
        jewels = []
        for i in range(a):
            jewels.append(V[i])
        for j in range(b):
            jewels.append(V[-(j + 1)])
        jewels = sorted(jewels)
        total = sum(jewels)
        if K - (a + b) <= 0:
            ans = max(total, ans)
            continue
        for i in range(K - a - b):
            if i < len(jewels) and jewels[i] < 0:
                total += abs(jewels[i])
        ans = max(total, ans)
print(ans)