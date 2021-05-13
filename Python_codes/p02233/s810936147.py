from collections import deque
from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

table = [0] * 45

table[0] = 1
table[1] = 1

for i in range(2,45):
    table[i] = table[i-1]+table[i-2]


N = int(input())
print("%d"%(table[N]))
