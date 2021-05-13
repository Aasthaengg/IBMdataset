while True:
    n, x = map(int, raw_input().split())
    if (n+x) == 0:
        break

    comb = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            c = i + j
            tmp = x - c
            if (tmp <= n) & (tmp > j):
                comb.append([i, j, tmp])

    print len(comb)