while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    cnt = 0
    for i in range(1, min(n - 1, int(x / 3))):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if (i + j + k) == x:
                    cnt += 1
    print(cnt)