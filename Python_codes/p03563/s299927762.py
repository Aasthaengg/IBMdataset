import sys
import  math
import bisect
from statistics import *
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

r = ni()
g = ni()
print(2 * g - r)