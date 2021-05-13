import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
from fractions import Fraction

N, K = map(int, input().split())
if N >= K*2-1:
    print('YES')
else:
    print('NO')
