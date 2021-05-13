#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
a,b=map(int,input().split())
if b%a==0:
    print(a+b)
else:
    print(b-a)