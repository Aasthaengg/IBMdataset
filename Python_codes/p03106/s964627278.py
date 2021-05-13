def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

A, B, K = map(int, input().split())

set_a = set(make_divisors(A))
set_b = set(make_divisors(B))
set_ab = set_a.intersection(set_b)

list_ab = list(set_ab)
list_ab.sort()
# print(list_ab)

print(list_ab[-K])