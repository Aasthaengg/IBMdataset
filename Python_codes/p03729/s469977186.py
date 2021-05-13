import sys
import copy
import  math
from _bisect import *
from collections import *
from operator import itemgetter
from math import factorial
"""
from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)
"""
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

a, b, c = input().split()
print('YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO')
