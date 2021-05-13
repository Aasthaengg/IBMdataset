import math

a, b, c, d = map(int, input().split())

x = math.ceil(c / b)
y = math.ceil(a / d)

if x <= y:
    print("Yes")
else:
    print("No")