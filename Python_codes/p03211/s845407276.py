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
#import bisect
s=input()
n=len(s)
res=900
for i in range(n-2):
    if abs(753-int(s[i:i+3]))<res:
        res=abs(753-int(s[i:i+3]))
print(res)