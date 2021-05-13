import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

l,r = MAP()
if(l%2019>=r%2019) or (r-l>=2018):
  print(0)
  exit()
else:
  l %= 2019
  r %= 2019

ans = inf
for i in range(l,r):
  for j in range(i+1,r+1):
    ans = min(ans, i*j%2019)

print(ans)