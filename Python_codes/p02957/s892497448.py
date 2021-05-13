import itertools
import math
import fractions
import functools
a, b = map(int, input().split())
if (b+a)/2 == (b+a)//2:
    print((b+a)//2)
else: print("IMPOSSIBLE")