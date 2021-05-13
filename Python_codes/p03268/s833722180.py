import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
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
N,K = map(int,input().split())
if K % 2 == 1:
    x = N // K
    print(x**3)
else:
    k = K // 2
    x = N // k
    if x % 2 == 0:
        y = x // 2
        print(2*(y**3))
    else:
        y = x // 2
        print(y**3+(y+1)**3)
