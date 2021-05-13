import sys
from functools import reduce
from math import sqrt

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    s = [int(i) for i in sys.stdin.readline().split()]
    m = sum(s) / n
    print(sqrt(sum(map(lambda x: (x - m) ** 2, s)) / n))