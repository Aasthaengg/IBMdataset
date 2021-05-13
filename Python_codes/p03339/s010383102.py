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
s=list(input())
ans=n
r=[0]*n
l=[0]*n
for i in range(1,n):
    if s[i-1]=="W":
        r[i]=r[i-1]+1
    else:
        r[i]=r[i-1]
    if s[n-i]=="E":
        l[n-1-i]=l[n-i]+1
    else:
        l[n-1-i]=l[n-i]
for i in range(n):
    ans=min(ans,l[i]+r[i])
print(ans)
