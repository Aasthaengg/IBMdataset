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
a=list(map(int,input().split()))
cnt=0
for i in a:
    while True:
        if i%2==0:
            cnt+=1
            i=i//2
        else:
            break
print(cnt)