import sys, heapq, bisect, math, fractions
from collections import deque

N, D = map(int, input().split())

i = 0
res = 0
while i < N:
    res += 1
    i += 2 * D + 1

print(res)