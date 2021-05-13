n, k = map(int, input().split())

max_val = (n - 1) * (n - 2) // 2

if n == 2 and k == 1:
    print(-1)
    exit()

if k > max_val:
    print(-1)
    exit()
else:
    cnt = (n - 1) * (n - 2) // 2 - k
    m = n - 1 + cnt
    print(m)
    for i in range(n-1):
        print(1, i+2)
    if cnt == 0:
        exit()
    tmp = 0

    for j in range(2, n + 1):
        for p in range(j + 1, n + 1):
            print(j, p)
            tmp += 1
            if tmp == cnt:
                exit()
