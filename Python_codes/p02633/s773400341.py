import math

x = input()
x = int(x)

lcd=(360*x)//math.gcd(360,x)

print(lcd//x)

