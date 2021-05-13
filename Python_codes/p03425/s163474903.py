import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def s(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")

n = k()
name = [s() for i in range(n)]
m = [i for i in name if i.startswith("M")]
a = [i for i in name if i.startswith("A")]
r = [i for i in name if i.startswith("R")]
c = [i for i in name if i.startswith("C")]
h = [i for i in name if i.startswith("H")]
ml,al,rl,cl,hl = len(m),len(a),len(r),len(c),len(h)

ans = ml*al*rl + ml*al*cl + ml*al*hl +ml*rl*cl + ml*rl*hl + ml*cl*hl + al*cl*hl + al*rl*cl + al*rl*hl + rl*cl*hl

print(ans)
