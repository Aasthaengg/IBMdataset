a, b, k = map(int, input().split())
if a + b <= k:
    print(0, 0)
else:
    print(0 if a < k else a - k, b + (a - k) if a < k else b)
