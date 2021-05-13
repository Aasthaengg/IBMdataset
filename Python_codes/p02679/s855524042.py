from math import gcd

mod = 1000000007

n = int(input())
counter = {}
zeros = 0
for i in range(n):
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        zeros += 1
        continue
    g = gcd(a, b)
    a //= g
    b //= g
    if (b < 0):
        a = -a
        b = -b
    if (b == 0 and a < 0):
        a = -a
    rot90 = a <= 0
    if rot90:
        a, b = b, -a
    count = counter.get((a, b), [0, 0])
    if rot90:
        count[0] += 1
    else:
        count[1] += 1
    counter[(a, b)] = count

ans = 1
for k, pairs in counter.items():
    s_count = pairs[0]
    t_count = pairs[1]
    now = pow(2, s_count, mod)-1
    now += pow(2, t_count, mod)-1
    now += 1
    ans *= now
    ans %= mod
print((ans - 1 + zeros) % mod)
