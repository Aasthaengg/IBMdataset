a, b, c,d = map(int, input().split())
import math
min = int(c*d/math.gcd(c,d))
x = b-b//c - b//d + b//min
y = a-1-(a-1)//c - (a-1)//d + (a-1)//min

print(int(x-y))