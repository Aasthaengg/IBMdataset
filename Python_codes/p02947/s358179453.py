import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
s = [sorted(input()) for i in range(n)]
s.sort()

cnt = 1
ans = 0
for i in range(1, n):
        if s[i] == s[i-1]:
                cnt += 1                
        else:
                ans += cnt*(cnt-1)//2
                cnt = 1
ans += cnt*(cnt-1)//2
print(ans)