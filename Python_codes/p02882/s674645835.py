import math

a, b, x = map(int, input().split(' '))

x = x / a


def f(t):
    tan = math.tan(t)
    if tan <= b / a:
        return (a * b) - (a * a * tan / 2)
    else:
        return b * (b / tan) / 2


left = 0.0
right = math.pi / 2

for i in range(10000):
    theta = (left + right) / 2
    if f(theta) >= x:
        left = theta
    else:
        right = theta

print(left / math.pi * 180)
