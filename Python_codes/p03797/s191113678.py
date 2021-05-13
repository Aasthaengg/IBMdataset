n, m = map(int, input().split())

if n < m // 2:
    res = n + (m - n * 2) // 4
    print(res)
else:
    res = m // 2
    print(res)
