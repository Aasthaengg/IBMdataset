ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil
s = list(input())
co = collections.Counter(s)
ls = []
for w in ["a","b","c"]:
    ls.append(co[w])
mx = max(ls)
f=True
for c in ls:
    if mx > c+1:
        f=False
yn(f)
