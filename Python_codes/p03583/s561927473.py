N = int(input())
for h in range(1,3500):
    for n in range(1,3500):
        flg = False
        try:
            w = (N*h*n)/(4*h*n-N*n-N*h)
            if w >= 0 and w.is_integer():
                flg = True
        except:
            pass
        if flg:
            print(h,n,int(w))
            exit(0)