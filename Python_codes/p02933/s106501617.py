"""
author : halo2halo
date : 10, Jan, 2020
"""

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = int(readline().decode('utf8'))
s = read().decode('utf8').rstrip()
print('red' if a < 3200 else s)
