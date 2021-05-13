import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
print(N * (N - 1) // 2)

