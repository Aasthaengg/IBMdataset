n = int(input())
t = [int(input()) for _ in range(n)]

import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

now = 1
for i in t:
    now = lcm(now,i)

print(now)