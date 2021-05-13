from sys import stdin
import numpy as np
import math

a,b,c = [int(x) for x in stdin.readline().rstrip().split()]

if a+b < c:
    print("No")
else:
    print("Yes")
