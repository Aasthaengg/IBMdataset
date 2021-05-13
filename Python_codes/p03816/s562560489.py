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
n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
cnt=0
for i in c:
    if c[i]%2==0:
        cnt+=1
if cnt%2==0:
    print(len(c))
else:
    print(len(c)-1)