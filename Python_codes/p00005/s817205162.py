import sys


def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def lcm(x, y):
    return int((x * y) / gcd(x, y))

for line in sys.stdin:
    l = line.replace('\n', '')
    a, b = l.split()
    a = int(a)
    b = int(b)
    print(gcd(a, b), lcm(a, b))