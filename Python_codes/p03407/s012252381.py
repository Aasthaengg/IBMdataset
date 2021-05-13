import sys
from statistics import *
from collections import *
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

a, b, c = na()
print('Yes' if a + b >= c else 'No')