import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
from fractions import Fraction

c = [0]*4
for i in range(3):
    a, b = map(int, input().split())
    c[a-1] += 1
    c[b-1] += 1
for i in range(4):
    if c[i] > 2:
        print('NO')
        exit()
print('YES')
