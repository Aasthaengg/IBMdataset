import math
a,b,c,d = map(int, input().split())
e = c*d//math.gcd(c,d)
# CでもDでも割り切れない -> Cで割り切れない＋Dで割り切れない - CとDで割り切れない
xa = math.ceil(a/c)-1
xb = b//c
ya = math.ceil(a/d)-1
yb = b//d
za = math.ceil(a/e)-1
zb = b//e
ans = (b-a+1)-(xb-xa)-(yb-ya)+(zb-za)
if ans >=0:
    print(ans)
else:
    print(0)