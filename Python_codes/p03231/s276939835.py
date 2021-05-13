from fractions import gcd

n, m = map(int, input().split())
s = list(map(str, input().rstrip()))
t = list(map(str, input().rstrip()))

g = gcd(n, m)

print(n * m // g if s[::n // g] == t[::m // g] else -1)