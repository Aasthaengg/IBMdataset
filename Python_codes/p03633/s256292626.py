#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
def lcm(a,b):
    g=gcd(a,b)
    res=g*(a//g)*(b//g)
    return res
l=int(input())
for i in range(n-1):
    ti=int(input())
    l=lcm(l,ti)
print(l)