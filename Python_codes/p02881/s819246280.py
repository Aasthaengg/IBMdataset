def enum_divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
    return res


N = int(input())
divs = enum_divisors(N)
ans = float("inf")
for div in divs:
    ans = min(ans, div + N // div - 2)
print(ans)
