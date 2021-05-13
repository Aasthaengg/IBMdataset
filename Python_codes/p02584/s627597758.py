y, k, d = map(int, input().split())
x = abs(y)
if k * d <= x:
    a = x - k * d
else:
    if x % d == 0:
        if (k - (x / d)) % 2 == 0:
            a = 0
        else:
            a = d
    else:
        b = x // d
        if (k - b) % 2 == 0:
            a = x - d * b
        else:
            a = -x + b * d + d
print(a)