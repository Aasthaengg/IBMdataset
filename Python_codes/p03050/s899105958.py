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
n=int(input())
if n==1:
    print(0)
    exit()
elif n==2:
  print(0)
  exit()
m=math.ceil(n/((n-1)**0.5+1))
ans=0
for i in range(1,m):
    if n%i==0:
        ans+=(n//i-1)
print(ans)