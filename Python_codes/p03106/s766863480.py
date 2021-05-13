import math
A, B, K = map(int, input().split())
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
divisors = make_divisors(math.gcd(A, B))
divisors.sort(reverse=True)
print(divisors[K-1])