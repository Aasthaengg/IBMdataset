a, b , k = map(int, input().split())

#約数取得
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

a_yakusu = make_divisors(a)
b_yakusu = make_divisors(b)
ab_yakusu = sorted(set(a_yakusu) & set(b_yakusu), reverse=True)

print(ab_yakusu[k-1])
