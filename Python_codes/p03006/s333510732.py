import sys
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
n=int(input())
l=[i for i in range(n)]
xy=[list(map(int,input().split()))  for _ in range(n)]
if n==1:
  print(1)
  exit()
comb=itertools.permutations(l,2)
dic={}
for c in comb:
    i,j=c
    xi,yi=xy[i]
    xj,yj=xy[j]
    p=xi-xj
    q=yi-yj
    if (p,q) not in dic:
        dic[(p,q)]=1
    else:
        dic[(p,q)]+=1
res=-1
ai=-1
for i in dic.keys():
    if res<dic[i]:
        ai=i
        res=dic[i]
print(n-dic[ai])