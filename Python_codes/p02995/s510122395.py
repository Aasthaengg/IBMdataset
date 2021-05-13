import math
a, b, c, d = map(int, input().split())

def lcm(m,n):
    return (m*n) // math.gcd(m,n)

if a%c == 0:
    x = a//c
else:
    x = a//c + 1

if a%d == 0:
    y = a//d
else:
    y = a//d + 1

if a%lcm(c,d) == 0:
    z = a//lcm(c,d)
else:
    z = a//lcm(c,d) + 1
    
X = b//c
Y = b//d
Z = b//lcm(c,d)
    
print((b-a+1) - ((X-x+1) + (Y-y+1) - (Z-z+1)))

