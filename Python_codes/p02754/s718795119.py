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
n,a,b=map(int,input().split())
ans=(n//(a+b))*a
r=n%(a+b)
if r<=a:
    print(ans+r)
else:
    print(ans+a)