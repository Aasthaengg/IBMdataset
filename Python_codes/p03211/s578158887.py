ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
import sys

s = input()
tmp=10**11
for i in range(0,len(s)-2):
    tmp = min(tmp,abs(753-int(s[i:i+3])))
print(tmp)
