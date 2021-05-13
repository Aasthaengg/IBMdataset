import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
n,k=map(int,input().split())
if k%2==1:
    num=n//k
    print(num**3)
else:
    num=n//k
    num2=(n-k//2)//k+1
    print(num**3+num2**3)