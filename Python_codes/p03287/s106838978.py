ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n,m = ma()
A= lma()
s = [0]*(n+1)
for i in range(n):
    s[i+1]=(s[i]+A[i])%m
co = collections.Counter(s)
ans = 0
for num,cnt in co.items():
    ans+=cnt*(cnt-1)//2
print(ans)
