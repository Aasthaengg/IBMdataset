from math import ceil
n, m = map(int, input().split())
a = ceil(n / (2 * m + 1))
print(a)
