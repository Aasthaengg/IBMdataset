#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

A, B = 1, 1
for x,y in L:
    n = max(0-(-A//x), 0-(-B//y))
    A, B = n*x, n*y

print(A+B)