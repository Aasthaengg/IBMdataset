from math import gcd
a, b, k = map(int, input().split())

g = gcd(a, b)

for i in range(g, 0, -1):
    if g % i == 0:
        k -= 1
        if k == 0:
            print(i)
            break
