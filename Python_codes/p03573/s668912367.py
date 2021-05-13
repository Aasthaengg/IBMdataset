from sys import stdin
import math
import bisect
import heapq
import numpy as np
from math import factorial
inf = 10**10

a,b,c = [int(x) for x in stdin.readline().rstrip().split()]

if a == b:
    print(c)
elif b == c:
    print(a)
else:
    print(b)