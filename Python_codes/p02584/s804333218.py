x, k, d = map(int, input().split())
maxi = k * d
res = x

if x < 0:
    x = abs(x)

if x - maxi >= 0:
    res = x - maxi
else:
    p = x % d
    m = p - d
    rest = k - (x // d)
    if rest % 2 == 1:
        res = m
    else:
        res = p

print(abs(res))