from math import gcd

n, m = map(int, input().split())
g = gcd(n, m)
s = input()
t = input()
f = True
for i in range(g):
    a = i * n // g
    b = i * m // g
    f &= (s[a] == t[b])

if f:
    print((n * m) // g)
else:
    print(-1)
