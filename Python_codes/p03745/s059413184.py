import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

d = [0] * N
for i in range(1, N):
    d[i] = A[i] - A[i - 1]

l = 0
r1 = 1
r2 = 1
ans = 0
while l < N:
    while r1 < N and d[r1] >= 0:
        r1 += 1
    while r2 < N and d[r2] <= 0:
        r2 += 1
    r = max(r1, r2)
    l = r
    ans += 1
    r1 = l + 1
    r2 = l + 1
print(ans)
