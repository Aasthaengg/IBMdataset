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
a,b,c=map(int,input().split())
print(max(a+10*b+c,10*a+b+c,10*c+a+b))