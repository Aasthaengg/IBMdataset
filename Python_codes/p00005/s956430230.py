import sys

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    print("{0} {1}".format(gcd(a, b), int((a * b) / gcd(a, b))))