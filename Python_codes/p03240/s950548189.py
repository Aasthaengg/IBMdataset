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
n=int(input())
xyh=[list(map(int,input().split())) for _ in range(n)]
xyh=sorted(xyh,key=lambda x:x[2])
for cx in range(101):
    for cy in range(101):
        h_a=h_b=10**10
        minh=10**10
        for i in range(n):
            x,y,h=xyh[i]
            if h!=0:
                h_a=h+abs(cx-x)+abs(cy-y)
                if h_a>minh:
                  break
                elif h_b!=10**10 and h_a!=h_b:
                    break
                else:
                    h_b=h_a
            else:
                minh=min(minh,abs(cx-x)+abs(cy-y))
                if minh==0:
                  break
        else:
            if minh==1 and h_a==10**10:
              print(cx,cy,1)
              exit()
            else:
                print(cx,cy,h_a)
                exit()
