N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        if (4*h*n-N*n-N*h) == 0:
            continue
        w = N*h*n // (4*h*n-N*n-N*h)
        if w < 1:
            continue
        if w*(4*h*n-N*n-N*h) == N*h*n:
            print(h, n, w)
            exit()
