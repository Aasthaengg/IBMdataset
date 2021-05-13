while 1:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    a =[]
    for i in range(1, n + 1):
        for j in range(2, n + 1):
            for k in range(3, n + 1):
                if i + j + k == x:
                    if i != j:
                        if j != k:
                            if i != k:
                                a.append([i, j, k])
    b = []
    for i in a:
        b.append(sorted(i))

    c = []
    c = sorted(b)

    if len(c) == 0:
        cnt = 0
    else:
        cnt = 1
        t = c[0]
        for i in c:
            if t != i:
                cnt += 1
                t = i
    print(cnt)