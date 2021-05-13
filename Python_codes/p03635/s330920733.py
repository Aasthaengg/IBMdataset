from sys import stdin
from itertools import groupby

a,b = [int(x) for x in stdin.readline().rstrip().split()]

print((a-1)*(b-1))