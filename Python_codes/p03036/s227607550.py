import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

r, D, x = map(int, input().split())
for i in range(10):
    x = r * x - D
    print(x)
