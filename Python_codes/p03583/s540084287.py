N = int(input())

L = 3500 + 1

for h in range(1, L):
    for n in range(1, h + 1):
        x = N * h * n
        y = 4 * h * n - N * (n + h)
        if y <= 0:
            continue
        if x % y == 0:
            w = x // y
            print(h, n, w)
            exit(0)
