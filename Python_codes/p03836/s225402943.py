import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy, copy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#import numpy as np
#from decimal import *

sx, sy, tx, ty = MAP()
X = tx - sx
Y = ty - sy

way1 = "R"*X + "U"*Y
way2 = "L"*X + "D"*Y
way3 = "L" + "U"*(Y+1) + "R"*(X+1) + "D"
way4 = "R" + "D"*(Y+1) + "L"*(X+1) + "U"

print(way1+way2+way3+way4)