import sys
from collections import defaultdict, deque
import bisect
from heapq import *
from math import factorial, ceil, floor
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# N, M, = map(int, input().split())
# N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# L = [list(input().strip())  for _ in range(N)]
# S = input().strip()

N, = map(int, input().split())
L = [[int(v) for v in input().split()] for _ in range(N)]

m = {}
for i in range(N):
    for j in range(N):
        if i != j:
            x, y = L[i]
            x2, y2 = L[j]

            key = (x - x2, y - y2)

            if m.get(key) == None:
                m[key] = 0
            m[key] += 1

if m == {}:
    print(1)
    exit()
print(N - max(m.values()))