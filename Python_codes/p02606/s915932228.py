import sys
import math
import collections
import decimal
import itertools
from collections import deque
from functools import reduce
import heapq
import copy
#n = int(input())
l, r, d = map(int, sys.stdin.readline().split())
#s = input()
#a = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(l, r+1):
    if i % d == 0:
        ans += 1

print(ans)
