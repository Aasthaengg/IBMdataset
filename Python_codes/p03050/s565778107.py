def divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
div = divisors(n)

ans = 0
for d in div:
    if d-1 == 0:
        continue
    if n%(d-1) == n//(d-1):
        ans += d-1
print(ans)