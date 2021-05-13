n, a, b = map(int, input().split())

ma = min(a, b)
if a + b - n < 0:
    mi = 0
else:
    mi = a + b - n

print(ma, mi)