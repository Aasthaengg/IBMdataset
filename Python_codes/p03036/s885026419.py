import itertools
import math
import fractions
import functools
import copy
r, d, x = map(int, input().split())

for i in range(10):
    x = r*x-d
    print(x)