import sys
import itertools
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
n = int(input())

print((n) * (n-1)//2)