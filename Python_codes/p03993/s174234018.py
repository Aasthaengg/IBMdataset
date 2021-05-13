import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

n = int(input())
a = list(map(int,input().split()))
pair = []
for i in range(len(a)):
    koho = [i,a[i]-1]
    koho.sort()
    pair.append(koho)
pair.sort()
cnt = 0
for i in range(len(pair)-1):
    if pair[i] == pair[i+1]:
        cnt+=1
print(cnt)