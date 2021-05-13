import sys
import math
import bisect
stdin = sys.stdin
mod = 10**9 + 7

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
sa = lambda h: [list(map(int, stdin.readline().split())) for i in range(h)]

a, b = na()
if b % a == 0:
    print(a+b)
else:
    print(b-a)