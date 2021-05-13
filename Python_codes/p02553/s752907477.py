import math as mt
import sys, string
from collections import Counter, defaultdict
input = sys.stdin.readline

# input functions
I = lambda : int(input())
M = lambda : map(int, input().split())
ARR = lambda: list(map(int, input().split()))

a, b, c, d = M()
print(max(a*c, a*d, b*c, b*d))