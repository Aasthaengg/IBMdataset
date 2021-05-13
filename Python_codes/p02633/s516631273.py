import math
x=int(input())
if 360%x==0:
    print(360//x)
else:
    print(360 // math.gcd(x, 360))