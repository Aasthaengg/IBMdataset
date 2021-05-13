import sys
import math

X = int(sys.stdin.readline())
for i in range(1, 10**5):
    if (X * i) % 360 == 0:
        print(i)
        break