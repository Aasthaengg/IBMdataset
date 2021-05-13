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
cnt=0
for i in range(n):
    x,y=map(int,input().split())
    if x==y:
        cnt+=1
    else:
        cnt=0
    if cnt>=3:
        print("Yes")
        break
else:
    print("No")
