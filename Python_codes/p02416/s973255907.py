from __future__ import division, print_function
from sys import stdin
for line in stdin:
    if line.startswith('0'):
        break
    print(sum(int(c) for c in line.rstrip()))