import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())
A = [0] * N
for i in range(N):
    x, y = map(int, input().split())
    A[i] = (x, y)

A = sorted(A)

d = defaultdict(int)
for i in range(N):
    x1, y1 = A[i]
    for j in range(i + 1, N):
        x2, y2 = A[j]
        d[(x2 - x1, y2 - y1)] += 1

freq = 0
for v in d.values():
    freq = max(freq, v)
print(N - freq)