def gcd(a, b):
    while(b > 0):
        a, b = b, a % b
    return a
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    g = gcd(a, b)
    print(g, a * b // g)