import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X, Y, A, B, C = map(int, readline().split())
P = sorted(map(int, readline().split()), reverse=True)
Q = sorted(map(int, readline().split()), reverse=True)
R = sorted(map(int, readline().split()), reverse=True)

Z = sorted(P[:X] + Q[:Y] + R, reverse=True)
print(sum(Z[:X + Y]))