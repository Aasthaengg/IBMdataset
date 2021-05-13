def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

N, A, B = getNM()
X = getList()
ans = 0
for i in range(N - 1):
    walk = X[i + 1] - X[i]
    ans += min(walk * A, B)
print(ans)