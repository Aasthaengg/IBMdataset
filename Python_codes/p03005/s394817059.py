import sys
from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())

if k == 1:
    print(0)
else:
    print(n-k)