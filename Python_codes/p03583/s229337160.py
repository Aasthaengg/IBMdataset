N = int(input())

if N%4 == 0:
    print(*[(3*N)//4]*3)
else:
    for w in range(1, 3501):
        for n in range(w+1, 3501):
            if 4*n*w - w*N - n*N <= 0:
                continue
            elif (n*w*N) % (4*n*w - w*N - n*N) == 0:
                h = (n*w*N) // (4*n*w - w*N - n*N)
                print(h, n, w)
                exit()