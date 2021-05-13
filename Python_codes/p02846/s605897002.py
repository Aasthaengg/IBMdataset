t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

p = (a1 - b1) * t1
q = (a2 - b2) * t2
if p > 0:
    p = -1 * p
    q = -1 * q

if p + q < 0:
    print(0)
elif p + q == 0:
    print('infinity')
else:
    s = -p // (p+q)
    t = -p % (p+q)
    if t == 0:
        print(2*s)
    else:
        print(2*s+1)