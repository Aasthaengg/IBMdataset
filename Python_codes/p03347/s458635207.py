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
a0=int(input())
if a0!=0:
    print(-1)
    exit()
ab=0
ans=0
for i in range(n-1):
    a=int(input())
    if a==ab+1:
        ans+=1
    elif a>ab+1:
        print(-1)
        exit()
    else:
        ans+=a
    ab=a
print(ans)