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
a = list(map(int, sys.stdin.readline().split()))

a.insert(0, 0)
ans = 0
for i in range(1, n+1):
    if i % 2 == 1:
        if a[i] % 2 == 1:
            ans += 1

print(ans)
