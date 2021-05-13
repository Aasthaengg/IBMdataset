N = int(input())
for h in range(1, 3501):
    for n in range(h, 3501):
        ok = 0
        ng = 3501
        while abs(ok-ng)>1:
            w = (ok+ng)//2
            if 4*h*n*w<=N*(n*w+w*h+h*n):
                ok = w
            else:
                ng = w
        if 4*h*n*ok==N*(n*ok+ok*h+h*n):
            print(h, n, ok)
            exit()