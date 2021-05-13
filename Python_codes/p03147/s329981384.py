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
H = list(map(int, input().split()))

X = [H]
ans = 0
while True:
    newX = []
    for group in X:
        f = min(group)
        ans += f
        A = [(h - f) for h in group]
        temp = []
        for a in A:
            if a == 0:
                if len(temp) > 0:
                    newX.append(temp)
                    temp = []
                continue
            temp.append(a)
        if len(temp) > 0:
            newX.append(temp)

    if len(newX) == 0:
        break
    X = newX
print(ans)
