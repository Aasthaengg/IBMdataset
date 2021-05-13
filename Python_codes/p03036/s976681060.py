from collections import Counter 
from collections import defaultdict
from collections import deque
import math
import itertools
import heapq
import sys
sys.setrecursionlimit(10**6)

#n=int(input())
#n,m=list(map(int,input().split()))
#a=list(map(int,input().split()))
input_list = lambda : list(map(int,input().split()))


a,b,c=input_list()
before=c
for _ in range(10):
    now=before*a-b
    print(now)
    before=now