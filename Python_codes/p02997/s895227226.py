n, k = map(int, input().split())
if (n - 2) * (n - 1) // 2 >= k:
    m = (n - 1) * n // 2 - k
    print(m)
    cnt = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            print(i, j)
            cnt += 1
            if cnt == m:
                exit()
else:
    print(-1)