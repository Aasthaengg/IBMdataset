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
a,b,k=map(int,input().split())
g=math.gcd(a,b)
d=[]
for i in range(1,int(pow(g,0.5))+1):
  if g%i==0:
    d.append(i)
    if g//i not in d:
      d.append(g//i)
d.sort(reverse=True)
print(d[k-1])