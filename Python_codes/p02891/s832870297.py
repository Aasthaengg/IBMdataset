import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

s = input()
k = INT()
ans = 0
cnt = 1
s = s + s

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
    else:
        ans += cnt // 2
        cnt = 1
ans += cnt // 2

if ans % 2 == 0 or ans == len(s)//2:
    print(ans*k//2)
else:
    print(ans//2+(ans+1)//2*(k-1))