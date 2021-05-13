from itertools import accumulate

n, k = map(int, input().split())
a = [0] + list(accumulate(map(int, input().split())))
print((max(a[i + k] - a[i] for i in range(n - k + 1)) + k) / 2)