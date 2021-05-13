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

A, B = map(int, readline().split())

MAX = max(A, B)

i = 2
setA = set()
setB = set()
while i ** 2 <= A:
    if A % i == 0:
        while A % i == 0:
            A //= i
        setA.add(i)
    i += 1
if A > 1:
    setA.add(A)
i = 2
while i ** 2 <= B:
    if B % i == 0:
        while B % i == 0:
            B //= i
        setB.add(i)
    i += 1
if B > 1:
    setB.add(B)

print(len(setA & setB) + 1)

