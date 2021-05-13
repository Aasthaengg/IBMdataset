import sys
import math
import collections
import decimal
import itertools
from collections import deque
from functools import reduce
import heapq
import copy
n = int(input())
#l, r, d = map(int, sys.stdin.readline().split())
#s = input()
#a = list(map(int, sys.stdin.readline().split()))

ans = [0 for i in range(n+1)]
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if i ** 2 + j ** 2 + k ** 2 + i * j + j * k + k * i > n:
                break
            
            ans[i ** 2 + j ** 2 + k ** 2 + i * j + j * k + k * i] += 1

for i in range(1, n+1):
    print(ans[i])
