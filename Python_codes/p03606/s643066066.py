"""
author : halo2halo
date : 30, Jan, 2020
"""

import sys

# import itertools
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(readline())
LR= [map(int, readline().split()) for _ in range(N)]


ans=0
for i,j in LR:
    ans+=j-i+1
    

print(ans)
