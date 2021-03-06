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

N, X = getNM()
A = getList()
ans = 0
flag = True
while flag:
    flag = False
    for i in range(N - 2):
        minus1 = A[i] + A[i + 1] - X
        minus2 = A[i + 1] + A[i + 2] - X
        if minus1 > 0 and minus2 > 0:
            minuspoint = min(minus1, minus2, A[i + 1])
            A[i + 1] -= minuspoint
            ans += minuspoint
            flag = True
between = [A[i] + A[i + 1] - X for i in range(N - 1)]
for i in between:
    if i > 0:
        ans += i
print(ans)
