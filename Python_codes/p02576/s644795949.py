n, x, t = map(int, input().split())
c = n // x
if n % x == 0:
    print(c * t)
else:
    print((c + 1) * t)