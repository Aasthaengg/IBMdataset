k, a, b = map(int, input().split())

if b - a <= 2: print(k + 1)
else:
    if k < a + 1: print(k + 1)
    else:
        q, r = divmod(k - a + 1, 2)
        print(a + q * (b - a) + r)