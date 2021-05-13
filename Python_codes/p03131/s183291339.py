n, a, b = map(int, input().split())

if a + 2 < b:
    if n < a:
        print(n + 1)
    else:
        n -= a - 1
        if n % 2 == 0:
            print(n//2 * (b - a) + a)
        else:
            print(n//2 * (b - a) + 1 + a)
else:
    print(n + 1)