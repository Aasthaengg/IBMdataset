n,a,b = map(int,input().split())
c = n // (a + b)
d = n % (a + b)
if d - a < 0:
    print((c * a) + d)
else:
    print((c * a) + a)