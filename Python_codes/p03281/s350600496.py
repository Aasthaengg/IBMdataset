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
import bisect
n=int(input())
ans=0
for i in range(1,n+1,2):
    s=set()
    for j in range(1,int(pow(i,0.5)+1)):
        if i%j==0:
            s.add(j)
            s.add(i//j)
    if len(s)==8:
        ans+=1
print(ans)