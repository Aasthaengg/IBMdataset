import sys
from math import gcd
input = sys.stdin.readline
X, Y = map(int, input().split())
g = gcd(X, Y)
if g != Y: print(X * Y // g + X)
else: print(-1)