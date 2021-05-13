ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil
x,y,z,k = ma()
A = lma()
B=lma()
C=lma()
AB = [a+b for a in A for b in B]
AB.sort(reverse=True)
C.sort(reverse=True)
ans=[]
iab=min(k,x*y)
ic=min(k,z)
for i in range(ic):
    for j in range(iab):
        ans.append(AB[j]+C[i])
ans.sort(reverse=True)
for i in range(k):
    print(ans[i])
