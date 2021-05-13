import itertools
import math
import fractions
import functools
import copy
a, b = map(int, input().split())
if a >= 13:
    print(b)
elif 6 <= a and 12 >= a:
    print(b//2)
else:
    print(0)