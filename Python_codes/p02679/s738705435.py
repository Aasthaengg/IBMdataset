import sys
from math import gcd
input = sys.stdin.readline

mod = 10 ** 9 + 7

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

d = {}
z = 0

pow_2 = [1]

for i in range(n):
    pow_2.append(pow_2[-1] * 2 % mod)

for a, b in ab:
    if a == 0 and b == 0:
        z += 1
        continue

    if a == 0 and b != 0:
        key = (0, 1)
    elif a * b > 0:
        g = gcd(a, b)
        key = (abs(a // g), abs(b // g))
    else:
        continue

    if key not in d:
        d[key] = [0, 0]
    d[key][0] += 1

for a, b in ab:
    if a != 0 and b == 0:
        key = (0, 1)
    elif a * b < 0:
        g = gcd(a, b)
        key = (abs(b // g), abs(a // g))
    else:
        continue
    
    if key in d:
        d[key][1] += 1


lo = n - z

ans = 1

for x, xi in d.values():
    if x * xi > 0:
        ans *= ((pow_2[x] - 1) + (pow_2[xi] - 1) + 1)
        ans %= mod
        lo -= x + xi

ans = (ans * pow_2[lo] + z - 1) % mod   

print(ans)


