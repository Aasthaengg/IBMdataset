ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
def divisor(n):
    d = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            d.append(i)
            if i != n//i:
                d.append(n//i)
    #d.sort()
    return d

n,k = ma()
A = lma()
s = sum(A)
ds = divisor(s);ds.sort(reverse=True)
for d in ds:
    ls = []
    cost=0
    for a in A:
        p,r = divmod(a,d)
        ls.append(r)
    ls.sort(reverse=True)
    s0 = sum(ls)
    cost=s0
    #print("d",d,"s0",s0,"ls",ls)
    for r in ls:
        if s0==0:
            break
        s0 -=d
        cost-=r
    if cost<=k:
        print(d)
        exit()
