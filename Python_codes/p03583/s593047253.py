N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        numera = 4 * h * n - n * N - h * N
        denomi = h * n * N
        if numera <= 0:
            continue
        elif denomi % numera != 0:
            continue
        w = denomi // numera
        print(h, n, w)
        exit()