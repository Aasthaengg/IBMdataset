from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
from functools import reduce

n,x,y = list(map(int, input().split()))

count = {}
for k in range(1,n):
    count[k] = 0

for i in range(1,n+1):
    for j in range(i+1,n+1):
        k = min([j-i, abs(x-i) + abs(y-j) + 1])
        count[k] += 1

for k in range(1,n):
    print(count[k])



