#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
s=list(input())
n=len(s)
s_set=set(s)
c=Counter(s)
dic=[]
for i in s_set:
    bef=-1
    delta=0
    if c[i]==1:
        continue
    else:
        for j in range(n):
            if  i==s[j]:
                res=j-bef-1
                bef=j
                delta = max(delta,res)
        res=n-1-bef
        dic.append(max(delta,res))
if not dic:
  print(n//2)
else:
  print(min(n//2,min(dic)))
