n, m = map(int, input().split())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return upper_divisors + lower_divisors[::-1]
m_divisor = make_divisors(m)
for i in m_divisor:
    if i <= m / n:
        print(i)
        exit()