n, a, b = map(int, input().split())
if abs(b - a) & 1:
    l = (a - 1) + (b - 1) + 1
    r = (n - a) + (n - b) + 1
    x = min(l, r)
else:
    x = abs(b - a)
print(x // 2)
