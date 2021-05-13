ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("POSSIBLE") if fl else print("IMPOSSIBLE")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil
gcd = math.gcd
n,k = ma()
A = lma()
mx = max(A)
tmp = A[0]
for a in A:
    tmp = gcd(a,tmp)
f=True

if mx<k:
    f=False
    yn(f)
    exit()
if tmp == 1:
    pass
else:
    if k%tmp==0:
        pass
    else:
        f=False
yn(f)
