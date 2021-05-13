def enum_divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res


N = int(input())
ans = 0
for i in enum_divisors(N):
    d = N // i - 1
    if d == 0 or N // d != N % d:
        continue
    ans += d
print(ans)
