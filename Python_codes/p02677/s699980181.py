from math import sin, cos, radians

A, B, H, M = map(int, input().split())

angleH = radians(90 - H / 12 * 360 - M / 60 * 30)
angleM = radians(90 - M / 60 * 360)
Hx, Hy = A * cos(angleH), A * sin(angleH)
Mx, My = B * cos(angleM), B * sin(angleM)

print(((Hx - Mx)**2 + (Hy - My)**2)**(0.5))
