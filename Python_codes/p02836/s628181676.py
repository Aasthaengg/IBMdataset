ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq

s = input()
sr = s[::-1]
l = len(s)
cnt=0
for i in range(l):
    if s[i] != sr[i]:
        cnt+=1
print(cnt//2)
