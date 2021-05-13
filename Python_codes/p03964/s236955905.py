def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

N = int(input())
s, t = 1, 1
for _ in range(N):
    a, b = map(int, input().split())
    g = gcd(a, b)
    a, b = a//g, b//g
    mi = max(-(-s//a), -(-t//b))
    s, t = a*mi, b*mi
print(s+t)