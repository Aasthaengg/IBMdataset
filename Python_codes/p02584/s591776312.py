x, k, d = map(int, input().split())

if x > 0:
    if x < k * d:
        if x // d % 2 == k % 2:
            g = x % d
        else:
            g = abs(d - (x % d))
    else:
        g = x - k * d
elif x == 0:
    if k % 2:
        g = d
    else:
        g = 0
else:
    if abs(x) < k * d:
        if abs(x) // d % 2 == k % 2:
            g = abs(x) % d
        else:
            g = abs(d - (abs(x) % d))
    else:
        g = abs(x) - k * d

print(g)
