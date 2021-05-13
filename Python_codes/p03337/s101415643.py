import sys
from collections import deque
from collections import  Counter
import statistics
import math

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

a, b = na()
print(max(a+b, a-b, a*b))

