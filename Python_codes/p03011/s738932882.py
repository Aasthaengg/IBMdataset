import itertools
import math
import fractions
import functools
import copy

p,q,r = map(int, input().split())
print(p+q+r-max(p,q,r))