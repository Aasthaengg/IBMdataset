N=int(input())
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-(n+h)*N>0 and (h*n*N)%(4*h*n-(n+h)*N)==0:
            print(n,h,(h*n*N)//(4*h*n-(n+h)*N))
            exit()
