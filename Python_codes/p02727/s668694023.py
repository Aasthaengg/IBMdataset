import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict
#d = defaultdict(int)
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import numpy as np
X,Y,A,B,C = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
s = p[:X]+q[:Y]+r
n = len(s)
for i in range(n):
    s[i] *= -1
heapify(s)
ans = 0
for i in range(X+Y):
    ans -= heappop(s)
print(ans)