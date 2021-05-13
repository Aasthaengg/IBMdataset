import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
x = LIST()
y = sorted(x)

b0 = y[n//2-1]
b1 = y[n//2]
for a in x:
  if a<=b0:
    print(b1)
  else:
    print(b0)