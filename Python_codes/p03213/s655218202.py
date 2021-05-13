from collections import Counter


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
c = Counter()

for i in range(2, n+1):
    c.update(prime_factorize(i))

d = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
for k, v in c.items():
    for size in [2, 4, 14, 24, 74]:
        if v >= size:
            d[size] += 1

total = 0
if d[4] >= 2 and d[2] >= 3:
    total += d[4] * (d[4] - 1) // 2 * (d[2] - 2)

if d[14] >= 1 and d[4] >= 2:
    total += d[14] * (d[4] - 1)

if d[24] >= 1 and d[2] >= 2:
    total += d[24] * (d[2] - 1)

if d[74] >= 1:
    total += d[74]

print(total)
