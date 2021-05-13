while True:
    a = 0
    n, x = [int(i) for i in input().split()]
    if n == x == 0:
        break

    s = 1
    m = s+1
    while not m == n:
        for e in range(m+1,n+1):
            result = s+m+e
            if result == x:
                a += 1
        m += 1
        if m == n:
            s += 1
            m = s+1

    print(a)