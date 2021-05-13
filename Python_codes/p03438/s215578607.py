#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sa=sum(a)
sb=sum(b)
if sb<sa:
    print("No")
else:
    cnt=sb-sa
    resa=0
    resb=0
    for i in range(n):
        if b[i]<a[i]:
            resa+=a[i]-b[i]
        else:
            resb+=math.ceil((b[i]-a[i])/2)
    if resa>cnt or resb>cnt:
        print("No")
    else:
        print("Yes")