def gcd(aa, bb):
    if aa % bb == 0:
        return bb
    return gcd(bb, aa % bb)

import sys
for line in sys.stdin.readlines():
    ab = list(map(int, line.split()))
    a = max(ab)
    b = min(ab)
    g = gcd(a, b)

    print(g, a * b // g)
