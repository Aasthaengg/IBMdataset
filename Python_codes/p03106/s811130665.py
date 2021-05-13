from math import gcd

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
    
a, b, k = map(int, input().split())
x = gcd(a, b)
l = make_divisors(x)
print(l[-k])