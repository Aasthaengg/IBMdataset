from sys import stdin
import math
import numpy as np
import itertools

a,b = [int(x) for x in stdin.readline().rstrip().split()]

if b >= a:
    print(0)
else:
    print(a-b)