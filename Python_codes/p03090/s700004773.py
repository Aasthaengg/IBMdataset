n = int(input())
if n % 2 == 0:
    n_edges = n * (n-1) // 2 - n // 2
    print(n_edges)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i + j + 2 == n + 1:
                continue
            else:
                print(i + 1, j + 1)
else:
    n_edges = n * (n - 1) // 2 - n // 2
    print(n_edges)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i + j + 2 == n:
                continue
            else:
                print(i + 1, j + 1)