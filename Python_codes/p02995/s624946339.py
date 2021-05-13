import math
 
def lcm(a, b):
    return (a*b)//math.gcd(a, b)
 
a, b, c, d = map(int, input().split())
e = lcm(c, d)
 
total = b - (a - 1)
cc = b//c - (a-1)//c
dd = b//d - (a-1)//d
ee = b//e - (a-1)//e
 
ans = total - cc - dd + ee
print(ans)