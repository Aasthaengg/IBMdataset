#import sys
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
ab=[list(map(int,input().split())) for _ in range(m)]
ab=sorted(ab,key=lambda x:x[1])
res=[]
res.append(ab[0][1]-1)
for i in range(1,m):
    a,b=ab[i]
    if a>res[-1]:
        res.append(b-1)
print(len(res))