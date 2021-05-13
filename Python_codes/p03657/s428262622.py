import sys
import copy
import  math
import bisect
from collections import *
from operator import itemgetter
"""
from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)
"""
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

a, b = na()
print('Possible' if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0 else 'Impossible')