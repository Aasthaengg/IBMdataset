import sys
import math

N, M = map(int, input().split())
a = map(int, input().split())
A = 0
for i in a:
    A += i

s = N - A
if s < 0:
    print(-1)
else:
    print(s)


