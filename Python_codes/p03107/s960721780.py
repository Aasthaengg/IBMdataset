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

from itertools import permutations
from math import factorial, hypot

# 結局最後には0の塊か1の塊が残る
S = list(map(int, list(input())))
zerocounter = 0
onecounter = 0
for st in S:
    if st == 0:
        zerocounter += 1
    else:
        onecounter += 1
print(min(zerocounter, onecounter) * 2)