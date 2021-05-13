from sys import stdin
import sys
import math
from functools import reduce
import itertools

h = int(stdin.readline().rstrip())

i = 1
while True:
    h = h // 2
    if h != 0: i += 1
    if h == 0: break

print(2**i-1)