import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)

#入力
n,a,b = map(int,input().split())
low = b + a*(n-1)
high = a + b*(n-1)
print(max(0,high - low +1))