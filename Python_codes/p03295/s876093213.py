import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,M = map(int,(input().split()))
c = []
bridge = []
nax = 0
for i in range(M):
    a,b = map(int,(input().split()))
    c.append((a,b))
c.sort(key=lambda x:x[1])

for i in range(M):
    if c[i][0] > nax:
        bridge.append(c[i][1]-1)
        nax = c[i][1]-1

print(len(bridge))