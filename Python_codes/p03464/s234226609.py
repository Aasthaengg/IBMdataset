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
k=int(input())
a=list(map(int,input().split()))
ml=mr=2
l=r=2
for i in range(k):
    ai=a[k-1-i]
    mr=(r//ai)*ai
    ml=(1+(l//ai))*ai if l%ai!=0 else l
    if ml>mr:
      print(-1)
      exit()
    if mr==0:
        print(-1)
        exit()
    elif ml==0:
        ml=mr
    l=ml
    r=mr+ai-1
print(l,r)