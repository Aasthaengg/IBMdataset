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
x=int(input())
for a in range(-10**3,10**3):
    for b in range(-10**3,a):
        if pow(a,5)-pow(b,5)==x:
            print(a,b)
            exit()