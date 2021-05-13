import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

A, P = map(int, input().split())
print((P + A * 3) // 2)

