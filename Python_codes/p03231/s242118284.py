import math

n,m = map(int,input().split())
a = input()
b = input()
g = math.gcd(n,m)
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