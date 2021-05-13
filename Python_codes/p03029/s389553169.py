import sys
import math

num = list(map(int,input().split()))

A = num[0]
P = num[1]
parts = A*3+P
print(math.floor(parts/2))
