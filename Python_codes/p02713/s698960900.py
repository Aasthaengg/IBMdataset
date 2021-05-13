K = int(input())
s = 0

cache = {}


def gcd(a, b):
    key = (a, b)
    r = cache.get(key, None)
    if r:
        return r
    while b != 0:
        a, b = b, a % b
    cache[key] = a
    return a


for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            a, b, c = tuple(sorted([i, j, k]))
            s += gcd(a, gcd(b, c))

print(s)
