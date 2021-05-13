N = int(input())

h = n = w = 1
for h in range(1, 3501):
    Nh = N*h
    for n in range(1, 3501):
        div = 4*h*n - N*n - Nh
        if div <= 0:
            continue
        if (Nh*n)%div==0:
            print(h,n,(Nh*n)//div)
            exit()
