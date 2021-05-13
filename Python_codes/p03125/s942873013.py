import itertools
import math
import fractions
import functools
import copy
a, b = map(int, input().split())
if b % a == 0:
    print(a+b)
else: print(b-a)