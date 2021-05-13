k, a, b = map(int, input().split())
if b - a <= 1:
    print(k + 1)
else:
    n = a
    n += int((k + 1 - a) / 2) * (b - a)
    n += (k + 1 - a) % 2
    print(n)