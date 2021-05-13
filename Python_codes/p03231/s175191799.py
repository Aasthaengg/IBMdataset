from math import gcd
n, m, S, T = open(0).read().split()
n, m = int(n), int(m)
l = n*m // gcd(n, m)

d = {}
t = l//n
for i in range(n):
    d[i*t] = S[i]
t = l//m
for i in range(m):
    if i*t not in d or d[i*t] == T[i]:
        d[i*t] = T[i]
    else:
        print(-1)
        break
else:
    print(l)