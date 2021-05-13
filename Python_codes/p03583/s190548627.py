N = int(input())
for n in range(1, 3501):
    for w in range(n, 3501):

        try:
            t = (N*n*w) % (4*n*w - N*w - N*n)
        except:
            continue

        if t == 0 and 4*n*w - N*w - N*n>=0:
            print((N*n*w) // (4*n*w - N*w - N*n), n, w)
            exit()
