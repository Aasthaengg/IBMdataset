import sys
from statistics import *
from collections import *
from operator import itemgetter

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

m = ni()
print(24 + 24 - m)