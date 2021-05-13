a, b, k = map(int, input().split())

def make_divisors(n): # 約数列挙
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

a_d = set(make_divisors(a))
b_d = set(make_divisors(b))
d = sorted(list(a_d & b_d), reverse=True)

print(d[k-1])