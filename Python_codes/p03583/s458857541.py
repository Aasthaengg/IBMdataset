N=int(input())
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-(h+n)*N>0:
            if (h*n*N)%(4*h*n-(h+n)*N)==0 and (h*n*N)//(4*h*n-(h+n)*N)>=1:
                print(h,n,(h*n*N)//(4*h*n-(h+n)*N))
                exit()
