from math import cos, pi, sqrt
A, B, H, M = map(int, input().split())
t = abs((H+M/60)/12 - M/60)*2*pi
print(sqrt(A**2 + B**2 - 2*A*B*cos(t)))