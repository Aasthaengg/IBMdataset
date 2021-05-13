from sys import stdin
from math import ceil
a, b = [int(x) for x in stdin.readline().rstrip().split()]

n = ceil((b-1)/(a-1))
print(n)