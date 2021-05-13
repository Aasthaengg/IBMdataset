N=int(input())
flag=0
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-n*N-h*N!=0:
            w = N*h*n/(4*h*n-n*N-h*N)
            if int(w)==w and 1<=w<=3500:
                print(h,n,int(w))
                flag = 1
                break
    if flag==1:
        break