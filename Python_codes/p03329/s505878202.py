def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N = getN()

num = [1]
sixsta = 6
while sixsta < 100000:
    num.append(sixsta)
    sixsta *= 6

ninesta = 9
while ninesta < 100000:
    num.append(ninesta)
    ninesta *= 9
num.sort()

dp = [float('inf')] * 100001
dp[0] = 0
for i in range(N + 1):
    for k in range(len(num)):
        if i >= num[k]:
            dp[i] = min(dp[i], dp[i - num[k]] + 1)
print(dp[N])
