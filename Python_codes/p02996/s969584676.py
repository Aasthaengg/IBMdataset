
import datetime
from decimal import Decimal, ROUND_DOWN
import heapq
from fractions import gcd
from functools import reduce
from collections import deque
# from math import factorial
import itertools
import collections
import math
import sys
sys.setrecursionlimit(2000000)
# import statistics
# import numpy as np
# n = int(input())
# n, m, p = list(map(int, input().split()))
# a = list(map(int, input().split()))
#
#  abc = [int(input()) for i in range(5)]
n = int(input())
# w = list(map(int, input().split()))
#A = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
ab = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
ab_sorted = sorted(ab, key=lambda x: x[1])
# print(ab_sorted)

total = 0
for i in range(n):
    total += ab_sorted[i][0]
    if total > ab_sorted[i][1]:
        print("No")
        exit()
print("Yes")
