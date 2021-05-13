def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


A, B, K = map(int, input().split())
A_yaku = make_divisors(A)
B_yaku = make_divisors(B)
A_B_yaku = sorted(list(set(A_yaku) & set(B_yaku)))
print(A_B_yaku[len(A_B_yaku) - K])
