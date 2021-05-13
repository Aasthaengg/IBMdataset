k, a, b = map(int, input().split())

if a + 2 > b or k < a:
    print(k + 1)
else:
    k -= (a - 1)
    have = a
    div, mod = divmod(k, 2)
    print((b - a) * div + a + mod)