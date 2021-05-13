import math
x = int(input())
s =  x * 360 / math.gcd(x, 360)
print(int(s//x))