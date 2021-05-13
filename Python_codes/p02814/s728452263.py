import fractions
from functools import reduce

n, m = map(int, input().split())
a = list(map(int, input().split()))

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def count_factorize(n):
    counter = 0
    while n % 2 == 0:
        counter += 1
        n //= 2
    return counter

mod = count_factorize(a[0])
for i in range(1, n):
    if count_factorize(a[i]) != mod:
        print(0)
        exit()
lcm_a = lcm(*a)
print(m // (lcm_a//2) - m // lcm_a)
