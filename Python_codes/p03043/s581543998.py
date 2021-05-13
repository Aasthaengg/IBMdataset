from decimal import Decimal 
n, k = map(int, input().split())
count = 0
p = 0

if n >= k:
    a = n
    p += Decimal((a - k + 1) / a)
    n = k
    for i in range(k, 1, -1):
        n = n / i * (i - 1)
        while n < k:
            n *= 2
            count += 1
        p += Decimal(1 / a * (1 / 2) ** count)
    print(p)
else:
    a = n

    while n < k:
        n *= 2
        count += 1
    p += Decimal(1 / a * (1/2) ** count)

    for i in range(a, 1, -1):
        n = n / i * (i - 1)
        while n < k:
            n *= 2
            count += 1
        p += Decimal(1 / a * (1 / 2) ** count)
    print(p)