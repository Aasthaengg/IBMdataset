n = int(input())


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


def is_favorite(n, m):
    if x == 0:
        return False
    else:
        return n // m == n % m


li = make_divisors(n)
li = [x - 1 for x in li]


ans = 0
for x in li:
    if is_favorite(n, x):
        ans += x

print(ans)