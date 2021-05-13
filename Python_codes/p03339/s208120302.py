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
S = input()
# up 左にいるWの人数
up = [0 for i in range(N)]
# down 右にいるEの人数
down = [0 for i in range(N)]

for i in range(1, N):
    if S[i - 1] == "W":
        up[i] = up[i - 1] + 1
    else:
        up[i] = up[i - 1]

for i in range(2, N + 1):
    if S[-i + 1] == "E":
        down[-i] = down[-i + 1] + 1
    else:
        down[-i] = down[-i + 1]
ans = float('inf')
for i in range(N):
    opt = up[i] + down[i]
    ans = min(ans, opt)
print(ans)