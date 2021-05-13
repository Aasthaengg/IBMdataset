import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
num = [0]*k
for i in reversed(range(1, k+1)):
    count = pow(k//i, n, MOD)
    for j in range(2, (k//i)+1):
        count = (count - num[j*i - 1])%MOD
    num[i-1] = count

# print(num)
print(functools.reduce(lambda s, x: ((x[0]+1) * x[1] + s)%MOD, enumerate(num), 0))
