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

s = input()

ans = 0
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        ans += 1

print(ans)