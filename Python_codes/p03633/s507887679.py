import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
t = [INT() for i in range(n)]
ans = t[0]

for x in t:
        ans = ans*x//gcd(ans, x)
print(ans)