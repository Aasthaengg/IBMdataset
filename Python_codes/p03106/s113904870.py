from math import gcd

a, b, k = map(int, open(0).read().split())

g = gcd(a, b)

cd = []

for i in range(1, g+1):
    if g%i==0:
        cd.append(i)

print(cd[-k])