import math

a, b, c, d = map(int, input().split())
cd = (c * d) // math.gcd(c, d)
u = b//c + b//d - b//cd
l = (a-1)//c + (a-1)//d - (a-1)//cd

print(b - a + 1 - u + l)
