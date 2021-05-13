n = int(input())


def factori(num):
    l = set()
    for i in range(1, int(num ** 0.5) + 1):
        if not num % i:
            l.add(i)
            l.add(n // i)
    return l


ans = 0
for m in factori(n):
    m -= 1
    if m > 0 and n == (n // m) * (m + 1):
        ans += m
print(ans)
