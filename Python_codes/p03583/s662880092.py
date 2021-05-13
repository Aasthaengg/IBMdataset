N=int(input())

for h in range(1,3501):
    for n in range(h,3501):
        x=(4*n*h-n*N-h*N)
        if x<=0 or n*h*N%x:continue
        print(h,n,n*h*N//x )
        exit()