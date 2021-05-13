from math import factorial as fac
a, b = map(int, input().split())
if abs(a-b) > 1:
    print(0)
    exit()
af = fac(a)
bf = fac(b)
sosu = 10**9+7
if a==b:
    print((af*bf*2)%sosu)
else:
    print((af*bf)%sosu)