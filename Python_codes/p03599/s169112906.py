import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
debugmode = False

a, b, c, d, e, f = MAP()
a *= 100
b *= 100
per = 0
ans = [str(a), '0']
for i in range(f // a + 1):
    for j in range((f - a * i) // b + 1):
        wtr = a * i + b * j
        rmn = f - wtr
        for k in range(rmn // c + 1):
            for l in range((rmn - c * k) // d + 1):
                sgr = c * k + d * l
                if wtr // 100 * e < sgr:
                    continue
                if wtr + sgr == 0:
                    continue
                tmp = 100 * sgr / (wtr + sgr)
                if wtr // 100 * e >= sgr and tmp > per:
                    per = tmp
                    ans = [str(wtr + sgr), str(sgr)]
print(' '.join(ans))