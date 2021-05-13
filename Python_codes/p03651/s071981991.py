import numpy as np
n, k = map(int, input().split())

a = list(map(int, input().split()))


def gcd(a, b):
    larger = max(a, b)
    smaller = min(a, b)

    if larger % smaller == 0:
        return smaller
    else:
        return gcd(smaller, larger % smaller)


m = int(np.max(a))

g = None

for i in range(n):
    if g is None:
        g = gcd(a[i], a[i])
    else:
        g = gcd(a[i], g)

if k % g == 0 and k <= m:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
