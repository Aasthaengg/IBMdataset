import sys
n, m = map(int, input().split())

if m % n == 0:
    print(m // n)
    sys.exit()


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


div = make_divisors(m)
div = [x for x in div if x <= m // n]

print(max(div))