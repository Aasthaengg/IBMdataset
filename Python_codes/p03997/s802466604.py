import sys
import copy
import math
import string
from _bisect import *
from collections import *
from operator import itemgetter
from math import factorial

from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)


stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

a = ni()
b = ni()
h = ni()
print((a + b) * h // 2)