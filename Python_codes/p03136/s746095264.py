import sys
import itertools
# import numpy as np
import time
import math
import heapq
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
# list(map(int, input().split()))

N = int(input())
L = list(map(int, input().split()))

mx = L[0]
idx = 0
for i in range(N):
    if L[i] > mx:
        mx = L[i]
        idx = i

if mx < sum(L[i] for i in range(N) if i != idx):
    print("Yes")
else:
    print("No")