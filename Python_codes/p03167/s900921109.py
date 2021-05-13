import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time
# import numpy as np
starttime = time.time()
# import numpy as np
mod = int(pow(10, 9) + 7)
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]

try:
    sys.setrecursionlimit(int(pow(10,6)))
    sys.stdin = open("input.txt", "r")
    # sys.stdout = open("../output.txt", "w")
except:
    pass


n,m=L()
A=[input() for i in range(n)]
dp=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            dp[i][j]=1
            continue
        if i==0:
            if A[i][j]==".":
                dp[i][j]=dp[i][j-1]
        elif j==0:
            if A[i][j]==".":
                dp[i][j]=dp[i-1][j]
        else:
            if A[i][j]==".":
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
            else:
                dp[i][j]=0
    # print(*dp[i])
print(dp[-1][-1])



endtime = time.time()
# print(f"Runtime of the program is {endtime - starttime}")

