def enum_divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res


N, M = map(int, input().split())
divs = filter(lambda x: x <= M // N, enum_divisors(M))
print(max(divs))
