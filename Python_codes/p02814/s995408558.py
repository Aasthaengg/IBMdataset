import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
N,M = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
flag = 0
order = 0
while True:
    for i in range(N):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            cnt += 1
    if cnt == 0:
        order += 1
        continue
    elif cnt == N:
        break
    else:
        print(0)
        flag = 1
        break
if flag == 0:
    S = a[0]
    for i in range(1,N):
        p = fractions.gcd(S,a[i])
        S = (S*a[i]) // p
    q = S*(2**(order-1))
    loc = M // q
    if loc % 2 == 1:
        loc += 1
    print(loc // 2)