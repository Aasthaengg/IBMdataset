def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


a, b, k = map(int, input().split())


set_a = set(make_divisors(a))
set_b = set(make_divisors(b))

both = list(set_a & set_b)
both.sort()

print(both[- k])