import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

S = '1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51'
A = list(map(int, S.replace(' ', '').split(',')))
print(A[int(input()) - 1])