a, b, k = map(int, input().split())
print(0 if a < k else a - k, max(0, b + (a - k)) if a < k else b)
