from math import gcd
n = int(input())
t = int(input())
ans = t
for i in range(n - 1):
    t = int(input())
    g = gcd(ans, t)
    ans *= t//g

print(ans)