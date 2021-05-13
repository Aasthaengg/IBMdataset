from bisect import bisect
n, m, x = map(int, input().split())
s = list(map(int, input().split()))

tmp = bisect(s, x)
print(min(tmp, m - tmp))