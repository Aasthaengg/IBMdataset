#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default
s=list(input())
n=len(s)
t=input()
m=len(t)
dic={}
ans=0
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]]=[i]
    else:
        dic[s[i]].append(i)
b=-1
for i in range(m):
    if t[i] not in dic:
        print(-1)
        exit()
    res=dic[t[i]]
    if res[-1]<=b:
        ans+=res[0]+1+(n-b-1)
        b=res[0]
    else:
        idx=bisect.bisect_right(res,b)
        ans+=res[idx]-b
        b=res[idx]
print(ans)