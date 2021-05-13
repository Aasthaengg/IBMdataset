N=int(input())

for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-N*n-N*h==0:
            continue
        if N*h*n%(4*h*n-N*n-N*h)==0:
            w=N*h*n//(4*h*n-N*n-N*h)
        else:
            continue
        if 4*h*n*w==N*(n*w+h*w+h*n) and w>0:
            print(h,n,w)
            exit()