from __future__ import division, print_function
from sys import stdin
from math import sqrt
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    data = [float(s) for s in stdin.readline().split()]
    m = sum(data) / len(data)
    print('{:.4f}'.format(sqrt(sum((s-m)**2 for s in data) / n)))