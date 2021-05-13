#!/usr/bin/env python3

import sys
from heapq import heapify, heappop, heappush
from math import ceil
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]

heapify(A)

for i in range(M):
    min_A = heappop(A)
    heappush(A, ceil(min_A/2))

print(-sum(A))

