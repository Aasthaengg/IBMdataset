import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, K = map(int, input().split())
X = list(map(int, input().split()))

ps = [0] + list(filter(lambda x: x >= 0, X))
ns = [0] + list(sorted(filter(lambda x: x < 0, X), reverse=True))

ans = INF
for i in range(len(ns)):
    val = abs(ns[i]) * 2
    if K - i >= 0 and K - i < len(ps):
        val += abs(ps[K - i])
        ans = min(ans, val)

for i in range(len(ps)):
    val = abs(ps[i]) * 2
    if K - i >= 0 and K - i < len(ns):
        val += abs(ns[K - i])
        ans = min(ans, val)
print(ans)
