import math

A, B, H, M = map(int, input().split())
angle = 30*H -5.5*M

CC = A**2 + B**2 - 2*A*B*math.cos(math.radians(angle))
print(CC**0.5)