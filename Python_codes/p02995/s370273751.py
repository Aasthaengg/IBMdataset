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
# n = int(input())
# w = list(map(int, input().split()))
A, B, C, D = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
# bc = [list(map(int, input().split())) for i in range(q)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))


def lcm(a, b):
    return int(a * b / gcd(a, b))


# b以下での個数
cb = B//C
db = B//D
cdb = B//(lcm(C, D))
total_b = cb+db-cdb

# a未満での個数
A -= 1
ca = A//C
da = A//D
cda = A//(lcm(C, D))
total_a = ca+da-cda


# print(total_a)
# print(total_b)
t = B-A
s = total_b-total_a
print(t-s)
