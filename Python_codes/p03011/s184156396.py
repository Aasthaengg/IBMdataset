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

a=input_list()
ans=float("inf")
for i in range(3):
    for j in range(i+1,3):
        ans=min(ans,a[i]+a[j])

print(ans)
