import sys
import itertools
import math

A,B,N = map(int, input().split())
a = 0

i = min(B-1,N)


print(math.floor(A*i/B) - A * math.floor(i/B))