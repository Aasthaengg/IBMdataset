import sys
from decimal import *
from math import floor

input = sys.stdin.readline
a,b = input().strip().split()
print(floor(Decimal(a)*Decimal(b)))
