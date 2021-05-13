import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
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
A = list(map(int,input().split()))
MOD = 10**9 + 7
ans = 1
count = [0]*N
for a in A:
    if a == 0:
        ans *= (3-count[0])
        ans = ans % MOD
        count[0]+= 1
    else:
        ans *= (count[a-1]-count[a])
        ans = ans % MOD
        count[a] += 1
print(ans%MOD)