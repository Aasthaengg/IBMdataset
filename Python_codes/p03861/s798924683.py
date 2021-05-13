import math
import sys
import numpy as np
from decimal import *
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
# ----------------------------------------
a, b, x = map(int, readline().split())

ans = Decimal(b // x) - Decimal(a // x)
if (a % x == 0):
    ans += 1

print(int(ans))
