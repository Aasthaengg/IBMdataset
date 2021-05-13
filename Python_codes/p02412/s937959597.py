while True:
    c = 0
    [n,x] = map(int,raw_input().split())
    if n == 0 and x == 0:
        break
    for p in range(1,n-1):
        for q in range(p+1,n):
            for s in range(q+1,n+1):
                if p + q + s == x:
                    c = c + 1
    print c