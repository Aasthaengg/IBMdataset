N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        div = 4*h*n - N*(h+n)
        if div!=0 and N*h*n%div==0:
            w = N*h*n // div
            if w > 0:
                print(h,n,w)
                exit()