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


x,a=input_list()
if x<a:
    print(0)

else:
    print(10)