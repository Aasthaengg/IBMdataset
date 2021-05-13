import math

n,m = map(int,input().split())
a = input()
b = input()
if a[0] != b[0]:
    print(-1)
    exit()

g = math.gcd(n,m)
if g == 1:
    print(n*m//g)
else:
    l = (n*m)//g
    d = {}
    for i in range(n):
        d[i*(l//n)] = a[i]
    for i in range(m):
        if i*(l//m) in d:
            if d[i*(l//m)] != b[i]:
                print(-1)
                exit()
    print(l)