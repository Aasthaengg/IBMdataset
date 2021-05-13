def divisor(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
ans = 0
for i in range(1, N + 1, 2):
    res = divisor(i)
    if len(res) == 8:
        ans += 1

print(ans)
