n, m = map(int, input().split())

mod = 10 ** 9 + 7

if abs(n - m) >= 2:
    print(0)
else:
    res = 1
    for i in range(1, n+1):
        res = res * i % mod
    for i in range(1, m+1):
        res = res * i % mod

    if abs(n - m) == 1:
        print(res)
    else:
        print(res * 2 % mod)