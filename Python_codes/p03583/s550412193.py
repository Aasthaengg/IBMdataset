N = int(input())
for h in range(N // 4, 3501):
    for n in range(N * h // max(1, (4 * h - N)), 3501):
        mod = 4 * h * n - N * (h + n)
        if mod > 0:
            w, r = divmod(N * h * n, mod)
            if r == 0:
                print(h, n, w)
                exit()