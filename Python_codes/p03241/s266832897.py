#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect

n,m=map(int,input().split())
x=int(pow(m,0.5))
res=[]
for i in range(1,x+1):
    if m%i==0:
        res.append(i)
        if i!=m//i:
            res.append(m//i)
res.sort()
ans=bisect.bisect_left(res,n)
print(m//res[ans])