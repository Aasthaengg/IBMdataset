import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

s = 'a' + input() + 'a'
n = len(s)
count = 0
ans = [0]*n
for i in range(1,n-1):
        if s[i] == 'R':
                count += 1
        elif s[i-1] + s[i] == "RL":
                ans[i-1] += (count+1)//2
                ans[i] += count//2
                count = 0
count = 0
for i in range(n-2,0,-1):
        if s[i] == 'L':
                count += 1
        elif s[i] + s[i+1] == "RL":
                ans[i+1] += (count+1)//2
                ans[i] += count//2
                count = 0
print(*ans[1:n-1])