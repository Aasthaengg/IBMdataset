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
n=int(input())
s=list(input())
c=Counter(s)
c=c.values()
ans=1
mod=10**9+7
for i in c:
    ans*=(i+1)
    ans%=mod
print(ans-1)