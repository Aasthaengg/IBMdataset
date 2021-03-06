import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for line in sys.stdin.readlines():
    a, b = map(int, line.split())
    print(gcd(a, b), a * b // gcd(a, b))