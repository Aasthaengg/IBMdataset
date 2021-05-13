from sys import stdin
from copy import deepcopy
from functools import reduce
from fractions import gcd
import math
import itertools
from collections import Counter
from itertools import chain  ##list(chain.from_iterable(l)) ##flatten
from heapq import heappush, heappop
import bisect

"""
N = int(input())
A, B = map(int,input().split())
A = list(map(int,input().split())) ## 横一列
A = [int(input()) for _ in range(N)] ## 縦一列
lst = [list(map(int,input().split())) for i in range(M)] ## 二次元
"""

N, S = map(int,input().split())
A = list(map(int,input().split()))

mod = 998244353

DP = [[0 for _ in range(S+1)] for _ in range(N+1)]
DP[0][0] = 1

for i in range(1, N+1):
  for j in range(S+1):
    if j - A[i-1] < 0:
      DP[i][j] = 2 * DP[i-1][j] % mod
    else:
      DP[i][j] = (DP[i-1][j-A[i-1]] + 2 * DP[i-1][j]) % mod
    
ans = DP[N][S]
print(ans)

#print(DP)