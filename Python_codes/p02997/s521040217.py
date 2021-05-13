n, k = map(int, input().split())


MAX_PAIR = (n-1)*(n-2)//2
if MAX_PAIR < k:
    print(-1)
else:
    m = n-1+MAX_PAIR-k
    print(m)
    for v2 in range(2, n+1):
        print(1, v2)
        m -= 1
    if m == 0:
        exit()

    for v in range(2, n):
        for v2 in range(v+1, n+1):
            print(v, v2)
            m -= 1
            if m == 0:
                exit()