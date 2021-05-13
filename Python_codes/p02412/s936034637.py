while True:
    (n, x) = map(int, input().split())
    if n == 0 and x == 0:
        break
    c = 0
    for i in range(1,n - 1):
        xi = x - i
        for j in range(i+1,n):
            if xi - j - j <= 0:
                break
            if xi - j <= n:
                c += 1
    print(c)