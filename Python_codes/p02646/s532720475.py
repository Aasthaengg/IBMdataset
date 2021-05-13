import sys
import math
import collections
import decimal
import itertools
from collections import deque
from functools import reduce
import heapq
#n = int(input())
a, v = map(int, sys.stdin.readline().split())
#s = input()
#a = list(map(int, sys.stdin.readline().split()))
     

b, w = map(int, sys.stdin.readline().split())
t = int(input())


if a > b:
    x = a - b
if b > a:
    x = b - a

if x <= t * (v-w):
    print("YES")
else:
    print("NO")
    



















