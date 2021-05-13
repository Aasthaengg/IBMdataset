import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
# import math
from fractions import gcd

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)


n = int(input())
A = list(map(int, input().split()))
sA = list(itertools.accumulate(A[::-1]))[::-1]
# print(sA)

num = 0
par = 1
for i in range(n+1):
    tmp_num = min(par, sA[i])
    if tmp_num <= 0:
        print(-1)
        exit()
    # print(tmp_num)
    num += tmp_num
    par = 2*(tmp_num-A[i])
    # print(par)

print(-1 if par < 0 else num)
