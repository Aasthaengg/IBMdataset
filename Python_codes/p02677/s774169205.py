from math import cos, sqrt, pi


A, B, H, M = map(int, input().split())
ang_A = (H * 60 + M) / 360 * pi
ang_B = (H * 60 + M) / 30 * pi
ang_C = abs(ang_A - ang_B)
if ang_C > pi:
    ang_C = 2 * pi - ang_C
C = sqrt(A**2 + B**2 - 2*A*B*cos(ang_C))
print(C)