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
ans = [0]*(N)
for i in range(N//2+1,N+1):
    ans[i-1] = a[i-1]
for i in range(1,N//2+1):
    j = N//2 +1-i
    s = 0
    for k in range(2*j,N+1,j):
        s += ans[k-1]
    s = s % 2
    ans[j-1] = (s - a[j-1])%2
ans2 = []
for i in range(N):
    if ans[i] == 1:
        ans2.append(i+1)
print(len(ans2))
print(*ans2)