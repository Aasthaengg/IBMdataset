n, d = map(int, input().split())
dd = (2 * d + 1)
m = n // dd
print(m + 1 if n % dd > 0 else m)