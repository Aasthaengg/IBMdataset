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
n=int(input())
s=input()
acc=[0]*(n+1)
ans=n
for i in range(n):
    if s[i]=="#":
        acc[i+1]=acc[i]+1
    else:
        acc[i+1]=acc[i]
for i in range(n+1):
    w=n-i-(acc[n]-acc[i])
    b=acc[i]
    ans=min(ans,w+b)
print(ans)