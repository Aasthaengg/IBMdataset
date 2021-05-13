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
ceil=lambda x,y: (x+y-1)//y
input_list = lambda : list(map(int,input().split()))
import fractions

#n=int(input())
a,b,t=input_list()

c=(t+0.5)//a

print(int(c*b))