import sys, heapq, bisect, math, fractions
from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(M)]

AB.sort(key=lambda x: x[1])
res = 0
bridge = 0

for a, b in AB:
    if not a <= bridge: 
        res += 1
        bridge = b - 1

print(res)
