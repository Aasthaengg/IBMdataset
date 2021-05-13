##import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n,m=map(int,input().split())
res=[[0]*8 for _ in range(n)]
ans=0
for i in range(n):
    x,y,z=map(int,input().split())
    res[i]=[x+y+z,x+y-z,x-y+z,x-y-z,-x+y+z,-x+y-z,-x-y+z,-x-y-z]
for i in range(8):
    c=0
    res=sorted(res,key=lambda x: x[i],reverse=True)
    for j in range(m):
        c+=res[j][i]
    ans=max(ans,c)
print(ans)