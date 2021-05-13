import sys
from math import atan2, pi

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
a, b, x = map(int, read().split())

s = x / a

if s > a*b/2:
    theta = atan2(2*(a*b-s), a**2)
else:
    theta = atan2(b**2, 2*s)

print(theta * 180 / pi)
