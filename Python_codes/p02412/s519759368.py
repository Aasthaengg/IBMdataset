while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0: break
    count = 0
    for i in range(1,n - 1):
        for j in range(i + 1 ,n):
            if i + j + j + 1 > x: break
            for k in range(j + 1 ,n + 1):
                if i + j + k == x:
                    count += 1
                    break
    print(count)