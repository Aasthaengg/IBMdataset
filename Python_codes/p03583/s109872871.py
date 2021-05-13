N = int(input())

# h <= 3N/4 <= N
for h in range(1, 3500 + 1):
    for n in range(1, 3500 + 1):
        if 4 * h * n - N * n - N * h == 0:
            continue
        w = (N * h * n) // (4 * h * n - N * n - N * h)
        if (N * h * n) % (4 * h * n - N * n - N * h) == 0 and w > 0:
            print(h, n, w)
            exit()