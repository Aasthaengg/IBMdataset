n, m, k = map(int, input().split())
if m > k:
    m, k = k, m
print(max(0, k-(m+n)))