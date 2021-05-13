import sys
import fractions

for line in sys.stdin.readlines():
    a, b = map(int, line.split())
    gcd = fractions.gcd(a, b)
    print(gcd, a * b // gcd)