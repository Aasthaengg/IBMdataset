def divisors(n):
    DIVISORS = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            DIVISORS.append(i)
            if i != n**0.5:
                DIVISORS.append(n // i)
    DIVISORS.sort()
    return DIVISORS


n, m = map(int, input().split())

A = divisors(m)

ans = 0
for a in A:
    if m // a >= n:
        ans = a

print(ans)
