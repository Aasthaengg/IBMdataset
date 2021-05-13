import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *
from fractions import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
h, w = map(int, input().split())
print(H * W - h * W - w * H + (h * w))

