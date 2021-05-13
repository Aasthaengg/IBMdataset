from sys import stdin, stdout
from time import perf_counter

import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7

a, b, x = map(int,input().split())

# y = ((b/x) -((a-1)/x))
print(((b//x) -((a-1)//x)))