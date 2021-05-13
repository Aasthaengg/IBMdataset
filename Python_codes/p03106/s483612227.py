from math import gcd

a, b, k = list(map(int, input().split()))
g = gcd(a, b)
l = []
i = 1
while i * i <= g:
    if g % i == 0:
        l.append(i)
        if i != g // i:
            l.append(g // i)
    i += 1
l.sort()
print(l[-k])
