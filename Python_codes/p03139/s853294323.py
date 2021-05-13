n, a, b = map(int, input().split())
mx = min(a, b)
mn = max(0, a + b - n)
print(mx, mn)
