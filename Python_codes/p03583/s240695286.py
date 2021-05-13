N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        mod = 4 * h * n - N * (h + n)
        if mod > 0:
            w, r = divmod(N * h * n, mod)
            if r == 0:
                print(h, n, w)
                exit()