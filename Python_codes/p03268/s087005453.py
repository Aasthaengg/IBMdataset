n, k = map(int, input().split())

if k % 2 != 0:
    print((n//k)**3)
else:
    kk = k//2
    a = 0
    b = 0
    for i in range(1, n+1):
        if i % kk == 0 and (i//kk) % 2 == 0:
            a += 1
        elif i % kk == 0 and (i//kk) % 2 != 0:
            b += 1
    print(a**3+b**3)
