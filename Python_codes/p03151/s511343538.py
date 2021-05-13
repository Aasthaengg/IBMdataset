import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
sys.setrecursionlimit(10 ** 6)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
a = LIST()
b = LIST()

if sum(a) < sum(b):
    print(-1)
else:
    c = sorted([a[i]-b[i] for i in range(n)])
    ans = 0
    reg = 0

    for x in c:
        if x < 0:
            ans += 1
            reg += x
        else:
            break

    for x in c[::-1]:
        if reg < 0:
            reg += x
            ans += 1
        else:
            break

    print(ans)