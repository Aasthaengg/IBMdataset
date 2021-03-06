def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


n = int(input())
divs = make_divisors(n)
ans = 10**12
for div in divs:
    x = n // div
    ans = min(x - 1 + div - 1, ans)
print(ans)
