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
from fractions import gcd
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

#############
# Main Code #
#############

N = getN()
cnt = 0
last_a = 0
first_b = 0
double = 0
for i in range(N):
    s = input()
    for j in range(len(s) - 1):
        if s[j] == 'A' and s[j + 1] == 'B':
            cnt += 1
    if s[0] == 'B' and s[-1] == 'A':
        double += 1
    elif s[0] == 'B':
        first_b += 1
    elif s[-1] == 'A':
        last_a += 1
opt = 0
if first_b == 0 and last_a == 0 and double != 0:
    opt = double - 1
else:
    opt = min(first_b + double, last_a + double)
print(cnt + opt)