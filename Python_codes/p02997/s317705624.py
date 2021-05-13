n, k = map(int, input().split())
if k > (n - 1) * (n - 2) // 2:print(-1)
else:
    m = (n - 1) * (n - 2)  // 2 - k
    print(n + m - 1)
    for i in range(2, n + 1):
        print(1, i)
    cnt = 0
    for i in range(2, n + 1):
        if cnt >= m:
            break
        for j in range(2, i):
            if cnt >= m:
                break
            print(i, j)
            cnt += 1