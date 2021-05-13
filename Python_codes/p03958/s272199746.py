import sys
input = sys.stdin.readline
from collections import *

K, T = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = sum(a[:-1])
print(max(0, a[-1]-1-s))