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
ans=0
for i in range(1,n):
    s1=set(s[:i])
    s2=set(s[i:])
    s1=s1.intersection(s2)
    ans=max(ans,len(s1))
print(ans)