import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
a = list(map(int,input().split()))
lcm = lcm_list(a)
d = [0]*n

for i in range(n):
    d[i] = lcm//a[i]

print(lcm/sum(d))