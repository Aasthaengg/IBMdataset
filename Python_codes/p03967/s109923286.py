import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
#from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
s=input()
n=len(s)
count=[0,0]
for i in s:
    if i=="g":
        count[0]+=1
    else:
        count[1]+=1
print((count[0]-count[1])//2)