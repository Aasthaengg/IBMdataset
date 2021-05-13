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
n,T=map(int,input().split())
ans=10000
for i in range(n):
    c,t=map(int,input().split())
    if t>T:
        continue
    if c<ans:
        ans=c
if ans==10000:
  print("TLE")
else:
  print(ans)