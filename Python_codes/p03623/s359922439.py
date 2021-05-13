import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
x,a,b=map(int,input().split())
if abs(x-a)<abs(x-b):
    print("A")
else:
    print("B")