import fractions
import sys
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
s = stdin.readline().rstrip()
t = stdin.readline().rstrip()


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


g = fractions.gcd(n, m)
for i in range(g):
    if s[n // g * i] != t[m // g * i]:
        print(-1)
        sys.exit()
print(lcm(n, m))