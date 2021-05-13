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

a,b=input_list()
ans=0
if a>12:
    ans=b
if 13>a and a>5:
    ans=b//2

print(ans)