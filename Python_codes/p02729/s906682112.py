n, m = map(int, input().split())

import math
def comb(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(comb(n,2) + comb(m,2))