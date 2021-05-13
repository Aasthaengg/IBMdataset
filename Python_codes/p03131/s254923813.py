k, a, b = map(int, input().split())

if a >= b:
    print(k + 1)
else:
    d = b-a
    if k < a or d // 2 <= 1:
        print(k + 1)
    else:
        t = k - (a - 1)
        print(a + t//2 * d + t % 2)
