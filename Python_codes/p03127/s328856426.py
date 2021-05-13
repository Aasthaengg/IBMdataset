#import sys
#import numpy as np
import fractions
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in range(1,n):
    ans=fractions.gcd(ans,a[i])
print(ans)