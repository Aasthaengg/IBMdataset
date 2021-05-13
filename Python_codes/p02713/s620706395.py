import math
from functools import reduce

k = int(input())

def find_gcd(*numbers):
    return reduce(math.gcd, numbers)

ans = 0
for a in range(1, k+1, 1):
    for b in range(1, k+1, 1):
        for c in range(1, k+1, 1):
            gcd = find_gcd(a, b, c)
            ans += gcd

print(ans)