from math import ceil, log2

n, k = map(int, input().split())
ans = sum(1 / 2 ** ceil(log2(k / i)) for i in range(1, min(n, k) + 1))
print((ans + max(0, n - k)) / n)