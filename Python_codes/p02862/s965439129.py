x, y = map(int, input().split())
if (x + y) % 3 != 0 or x * 2 < y or y * 2 < x:
    print(0)
else:
    n = (x + y) // 3
    r = y - n
    mod = 1000000007

    facn = 1
    facr = 1
    facnr = 1
    for i in range(1, n + 1):
        facn = (facn * i) % mod
        if i == r:
            facr = facn
        if i == n - r:
            facnr = facn
    
    b = 1
    invfacr = 1
    invfacnr = 1
    while b <= mod:
        if b & (mod - 2) != 0:
            invfacr = (invfacr * facr) % mod
            invfacnr = (invfacnr * facnr) % mod
        facr = (facr * facr) % mod
        facnr = (facnr * facnr) % mod
        b *= 2

    print((facn * invfacr * invfacnr) % mod)
