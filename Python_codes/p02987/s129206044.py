ma = lambda :map(int,input().split())
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

s = input()
co = collections.Counter(list(s))
f =True
if len(co) ==2:
    for it,cnt in co.items():
        if cnt!=2:
            f=False
else:f=False
yn(f)
