ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n= ni()
ab = []
dif = []
for i in range(n):
    a,b = ma()
    ab.append((a,b))
    dif.append((a+b,i))
dif.sort(reverse=True)
tak = 0
ao = 0
for i in range(n):
    d,idx = dif[i]
    if i%2==0:
        tak+=ab[idx][0]
    else:
        ao+=ab[idx][1]
print(tak-ao)
#print(tak,ao)
