N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        if 4*h*n != N*(n+h):
            x = N*h*n
            y = 4*h*n - N*(n+h)
            w = x // y
            if x % y == 0 and 1 <= w <= 3500:
                print(h, n, w)
                exit()

