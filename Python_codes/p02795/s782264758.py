#A
import math
h = int(input())
w = int(input())
n = int(input())
if h < w:
    a = w
else:
    a = h
print(math.ceil(n/a))