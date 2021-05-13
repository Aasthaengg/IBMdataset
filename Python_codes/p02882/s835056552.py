import math
a,b,x = map(int,input().split())

menseki = a * a
V = menseki * b

if V <= 2 * x:
    ans = (2 * (V - x)) / (a ** 3)
    degree = math.degrees(math.atan(ans))
    print(degree)
else:
    ans = (a * b * b) / (2 * x)
    degree = math.degrees(math.atan(ans))
    print(degree)