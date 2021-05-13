y, k, d = map(int, input().split())
x = abs(y)
i = int(x / d)
if i >= k:
    p = x - k * d
elif i == x / d:
    if (i + k) % 2 == 0:
        p = 0
    else:
        p = d
else:
    if ((2 * i + 1) * d == 2 * x) or ((i + k) % 2 == 0):
        p = x - i * d
    else:
        p = (i + 1) * d - x
print(int(p))