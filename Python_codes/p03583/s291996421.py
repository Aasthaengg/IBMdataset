N=int(input())

for i in range(N//4,3501):
    for j in range(N//4,3501):
        if not 4*i*j-(i+j)*N<=0:
            if (i*j*N)%(4*i*j-(i+j)*N)==0:
                print(i,j,(i*j*N)//(4*i*j-(i+j)*N))
                exit()