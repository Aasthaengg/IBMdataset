from bisect import bisect
_, m, x = map(int, input().split())
a = list(map(int, input().split()))
i = bisect(a, x)
print(min(i, m - i))