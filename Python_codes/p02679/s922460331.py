N = int(input())
AB = [[int(_) for _ in input().split()] for i in range(N)]

from math import gcd

def normalize(x, y):
    if x == 0 and y == 0:
        return (0, 0)
    if x == 0:
        return (0, 1)
    if y == 0:
        return (1, 0)
    if x < 0:
        x, y = -x, -y
    d = gcd(x, y)
    return (x // d, y // d)

def rev(x, y):
    x, y = -y, x
    if x < 0:
        x, y = -x, -y
    return x, y

xs = {}
xszero = 0

for a, b in AB:
    if a == 0 and b == 0:
        xszero += 1
        continue
    nab = normalize(a, b)
    rab = rev(*nab)
    if nab in xs:
        xs[nab][0] += 1
    elif rab in xs:
        xs[rab][1] += 1
    else:
        xs[nab] = [1, 0]

M = 1000000007

result = 1
for ab, nm in xs.items():
    k = (pow(2, nm[0], M) + pow(2, nm[1], M) - 1) % M
    result = (result * k) % M

print((result - 1 + xszero) % M)
