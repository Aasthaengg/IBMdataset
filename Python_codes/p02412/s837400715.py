while True:
    n, x = map(int, input().split())
    count = 0
    if not(n or x):
        break
    for i in range(1, n-1, 1):
        for j in range(i+1, n, 1):
            k = x - i -j
            if k > j and k <= n:
                count += 1
    print(count)