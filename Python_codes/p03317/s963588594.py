from bisect import bisect_left

n, k = map(int, input().split())
a = list(map(int, input().split()))

pos = bisect_left(a, 1)
print((pos + k - 2) // (k - 1) + (n - pos + k - 3) // (k - 1))