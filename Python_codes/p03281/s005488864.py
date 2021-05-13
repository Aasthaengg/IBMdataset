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

def resolve():
    N = int(input())
    ans = 0
    for i in range(1, N+1, 2):
        tmp = make_divisors(i)
        if len(tmp) == 8:
            ans += 1
    print(ans)
    return

resolve()