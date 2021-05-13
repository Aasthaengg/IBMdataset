N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        if (4*h*n-N*(h+n)) != 0:
            w = N*h*n/(4*h*n-N*(h+n))
            if float.is_integer(w) and w > 0:
                print(h, n, int(w))
                exit()
