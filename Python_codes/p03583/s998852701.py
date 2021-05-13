N = int(input())

for h in range(1, 3501):
    for n in range(h, 3501):
        x = 4*h*n-N*n-N*h
        if x <= 0:
            continue
        else:
            if (N*h*n)%x == 0:
                print(h, n, (N*h*n)//x)
                exit()
