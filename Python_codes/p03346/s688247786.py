import sys
from collections import defaultdict, deque
import bisect
from heapq import *
from math import factorial, ceil, floor
from collections import defaultdict
import itertools
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
L = [int(input()) for _ in range(N)]

f = False
t = defaultdict(int)
for i in range(N):
    if t[L[i] - 1] != 0:
        t[L[i]] = t[L[i] - 1] + 1
        t[L[i] - 1] = 0
    else:
        t[L[i]] = 1

print(N - max(t.values()))