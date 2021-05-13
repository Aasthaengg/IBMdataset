from fractions import gcd
a, b = map(int, input().split())

ans = (a * b) // gcd(a, b)
print(ans)
