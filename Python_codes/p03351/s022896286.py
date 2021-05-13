from sys import stdin
import bisect
from itertools import accumulate
import numpy as np

a,b,c,d= [int(x) for x in stdin.readline().rstrip().split()]

if abs(a-c) <= d:
    print("Yes")
elif abs(a-b)<= d and abs(b-c) <= d:
    print("Yes")
else:
    print("No")