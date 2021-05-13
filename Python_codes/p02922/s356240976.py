import math

A, B = [int(i) for i in input().split()]

B2 = B - A
A2 = A - 1
print(math.ceil(B2 / A2) + 1)
