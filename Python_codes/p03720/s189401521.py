import sys
import numpy as np
import collections as cl
import itertools as it
# import more_itertools as mit
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(100000)

n, m = map(int, readline().split())
A = []
B = []
for _ in range(m):
    a, b = map(int, readline().split())
    A.append(a)
    B.append(b)
for i in range(n):
    print(A.count(i+1)+B.count(i+1))