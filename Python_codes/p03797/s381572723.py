n, m = map(int, input().split())

if n > m // 2:
    print(m // 2)
else:
    print((2 * n + m) // 4)