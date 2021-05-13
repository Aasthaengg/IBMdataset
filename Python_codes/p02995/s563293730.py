import math
a,b,c,d = map(int,input().split())
a -= 1
ans = b-a
ans -= b//c - a//c
ans -= b//d - a//d
e = c*d//math.gcd(c,d)
ans += b//e - a//e
print(ans)
