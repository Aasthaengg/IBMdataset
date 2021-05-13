a, b = map(int, input().split())

import fractions
g = fractions.gcd(a, b)
print(a * b // g)