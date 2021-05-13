n, k = map(int, input().split())
kmax = (n - 1) * (n - 2) // 2
if k > kmax:
    print(-1)
else:
    rest = kmax - k
    print(n - 1 + rest)
    for i in range(1, n):
        print(i, n)
    i, j = 1, 2
    while rest:
        print(i, j)
        j += 1
        if j == n:
            i += 1
            j = i + 1
        rest -= 1