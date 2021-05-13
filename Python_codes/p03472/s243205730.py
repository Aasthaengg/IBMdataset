import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces


N, H = na()
maxA = -1
bbb = []
for i in range(N):
    a, b = na()
    maxA = max(maxA, a)
    bbb.append(b)
bbb.sort(reverse=True)
ct = 0
now = 0
for i in range(N):
    if bbb[i] <= maxA:
        break
    now += bbb[i]
    ct += 1
    if now >= H:
        print(ct)
        sys.exit()

res = H - now
if res % maxA == 0:
    print(ct + res // maxA)
else:
    print(ct + res // maxA + 1)