import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
# from math import gcd
# import itertools as it
# import collections
# from collections import deque 

def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------
s = inps()
if s[-1] == "s":
  s += "es"
else:
  s += "s"
print(s)