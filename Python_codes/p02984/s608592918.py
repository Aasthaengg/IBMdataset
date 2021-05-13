import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
N = int(input())
a = list(map(int,input().split()))
b = [0]*N
b0 = a[0]
b1 = a[0]
for i in range(1,N):
    c = a[i]
    if i % 2 == 0:
        b0 += c
        b1 -= c
    else:
        b0 -= c
        b1 += c
b[0] = b0
b[1] = b1
for i in range(2,N):
    b[i] = b[i-2] - 2*a[i-2]+2*a[i-1]
print(*b)