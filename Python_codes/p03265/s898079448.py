import sys
import copy
import math
import itertools
import numpy as np

l = [int(c) for c in input().split()]
a = l[0]
b = l[1]
c = l[2]
d = l[3]
x = c - a
y = d - b
print(c-y,d+x,a-y,b+x)
