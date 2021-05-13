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
s=input()
k=int(input())
c=0
for a in s:
    if a!="1":
        ans=a
        break
    else:
        c+=1
if k<=c:
    print(1)
else:
    print(ans)