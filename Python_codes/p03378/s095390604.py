from bisect import bisect_left

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

y = bisect_left(a, x)
print(min(y, m-y))