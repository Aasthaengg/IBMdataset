import math
a,b,c,d = map(int, input().split())
ans = b - a + 1
cntc = b//c - (a-1)//c
cntd = b//d - (a-1)//d
cd = (c * d) // math.gcd(c, d)
cntcd = b//cd - (a-1)//cd
ans = ans - cntc - cntd + cntcd
print(ans)