while True:
    n, x = (int(x) for x in input().split())
    if (n, x) == (0, 0): break
    cnt = sum(1 for i in range(1, n+1) for j in range(i+1, n+1) for k in range(j+1, n+1) if i + j + k == x)
    print(cnt)