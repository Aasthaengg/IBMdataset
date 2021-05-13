N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        y = (4 * h * n - N * (h + n))
        if 0 < y:
            x = (N * h * n)
            w, mod = divmod(x, y)
            if mod == 0:
                print(h, n, w)
                exit()