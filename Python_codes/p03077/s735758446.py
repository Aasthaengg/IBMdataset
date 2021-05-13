from math import ceil
n, a, b, c, d, e = [int(input()) for _ in range(6)]
neck = min(a, b, c, d, e)
ans = ceil(n / neck) + 4
print(int(ans))