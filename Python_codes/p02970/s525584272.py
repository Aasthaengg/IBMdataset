from math import ceil
n, d = [int(x) for x in input().split()]
ans = ceil(n / (2 * d + 1))
print(ans)