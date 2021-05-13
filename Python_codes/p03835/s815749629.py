##import sys
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
k,s=map(int,input().split())
ans=0
for i in range(k+1):
    if s-i>2*k:
        continue
    else:
        for j in range(k+1):
            if s-i-j>k or s-i-j<0:
                continue
            else:
                ans+=1
print(ans)