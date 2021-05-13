import math
import calendar
import fractions
import itertools

x, a, b = map(int, input().split())

if abs(a - x) > abs(b - x):
    print("B")
else:
    print("A")
