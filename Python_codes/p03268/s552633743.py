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

N, K, = map(int, input().split())

m = [0] * K
for v in range(1, N + 1):
    m[v % K] += 1

ans = 0
for v in range(1, K + 1):
    b = (K - v) % K
    c = (K - v) % K
    if (b + c) % K != 0:
        continue
    ans += m[v % K] * m[b] * m[c]
print(ans)