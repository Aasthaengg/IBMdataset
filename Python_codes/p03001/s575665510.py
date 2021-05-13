import itertools
import math
import fractions
import functools
import copy

w, h, x, y = map(int, input().split())
ans = 0
if x == w / 2 and y == h / 2:
    ans = 1

print(w*h/2,ans)
