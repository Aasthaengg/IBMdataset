D,N = map(int,input().split())

if D == 0:
    if N  == 100:
        print(N+1)
    else:
        print(N)
elif D==1:
    if N == 100:
        print((100 * N )+ 100)
    else :
        print(100*N)
else:
    if N ==100:
        print((10000*N)+10000)
    else:
        
        print(10000*N)
