import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections


n = int(input())
a = list(map(int,input().split()))
n1 = 0
n2 = 0
n4 = 0
for i in range(n):
    if a[i]%4 == 0:
        n4+=1
    elif a[i]%2 == 0:
        n2 +=1
    else:
        n1+=1

if n2 == 1:
    n2 = 0

if n4*2 + n2 >= n or n4*2 + 1 == n:
    print("Yes")
else:
    print("No") 