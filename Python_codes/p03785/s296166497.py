import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, c, k = MAP()
t = sorted(list(INT() for i in range(n)))

ans = 0
num = 0
time = inf
for i in range(n):
        if t[i]<=time+k and num < c:
                num += 1
        elif t[i]>time+k or num == c:
                ans += 1
                num = 1
                time = inf
        time = min(time, t[i])
ans += 1
print(ans)