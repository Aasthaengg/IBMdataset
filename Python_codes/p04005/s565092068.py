import math
import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
x = (a//2)*b*c
x = abs(abs(x-a*b*c)-x)
y = (b//2)*a*c
y = abs(abs(y-a*b*c)-y)
z = (c//2)*a*b
z = abs(abs(z-a*b*c)-z)

print(min(x, y, z))