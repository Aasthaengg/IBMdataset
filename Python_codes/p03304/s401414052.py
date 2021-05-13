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
import bisect
n,m,d=map(int,input().split())
if d!=0:
    ans=2*(m-1)*(n-d)/(n**2)
    print(ans)
else:
    ans=(m-1)/n
    print(ans)