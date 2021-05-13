def resolve():
    n, m, k = map(int, input().split())
    for x in range(n + 1):
        for y in range(m + 1):
            met = y * (n - x) + x * (m - y)
            if met == k:
                print('Yes')
                return

    print('No')
resolve()