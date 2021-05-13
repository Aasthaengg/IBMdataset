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

N = int(input())
A = [0] * N
for i in range(N):
    x, y, h = map(int, input().split())
    A[i] = (x, y, h)

for cx in range(101):
    for cy in range(101):
        candidates = set()
        for x, y, h in A:
            h += abs(x - cx) + abs(y - cy)
            candidates.add(h)
        for H in candidates:
            for x, y, h in A:
                if h != max(H - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, H)
                exit()