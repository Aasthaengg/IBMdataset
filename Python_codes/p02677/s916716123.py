import math

A,B,H,M = map(int, input().split())

angle_M = M*(360/60)
angle_H = H*(360/12)+angle_M/12

delta = min(abs(angle_H-angle_M),360-abs(angle_H-angle_M))

dist = math.sqrt(A*A + B*B -2*A*B*math.cos(math.radians(delta)))

print(dist)