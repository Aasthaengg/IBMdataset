import math

n, m = [int(i) for i in input().split()]
x = 1900 * m + 100 * (n - m)
p = 0.5 ** m
print(math.ceil(x / p))
