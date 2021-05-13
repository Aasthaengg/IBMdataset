while 1:
    n, x = map(int,raw_input().split())
    if n == x == 0:
        break
    sum = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            k = x - i - j
            if k > j and k <= n:
                sum += 1
    print sum