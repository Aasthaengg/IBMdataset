#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
s=input()
t=input()
n=len(s)
x={}
y={}
for i in range(n):
    if s[i] not in x:
        x[s[i]]=set([i])
    else:
        x[s[i]].add(i)
    if t[i] not in y:
        y[t[i]]=set([i])
    else:
        y[t[i]].add(i)
a=set()
b=set()
for i in x.values():
  if i not in y.values():
    print("No")
    break
else:
  print("Yes")