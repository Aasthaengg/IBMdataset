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
#import bisect
n=int(input())
s=[input() for _ in range(n)]
d={"M":0,"A":0,"R":0,"C":0,"H":0}
l=itertools.combinations(["M","A","R","C","H"],3)
for i in range(n):
    if s[i][0] in d:
        d[s[i][0]]+=1
ans=0
for i in l:
    a,b,c=i
    ans+=d[a]*d[b]*d[c]
print(ans)