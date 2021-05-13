import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

X, A = map(int, input().split())
print(0 if X < A else 10)
