a, b, x = map(int, input().split())

import math

theta1 = math.atan((b - x/a**2)*2/a)
theta2 = math.atan((a*b**2/(2*x)))
if b < a*math.tan(theta2):
    theta = theta2
else:
    theta = theta1

print(math.degrees(theta))