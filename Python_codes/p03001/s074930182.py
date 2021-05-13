from collections import Counter 
from collections import defaultdict
from collections import deque
import math
import itertools
import heapq
import numpy as np
import sys
sys.setrecursionlimit(10**6)

#n=int(input())
#n,m=list(map(int,input().split()))
#a=list(map(int,input().split()))
input_list = lambda : list(map(int,input().split()))


w,h,x,y=input_list()
ans=w*h/2
mul=0
if w==x*2 and h==y*2:
    mul=1

print(ans,mul)