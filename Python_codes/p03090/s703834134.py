N=int(input())
if N&1==1:
    M=(N-1)*(N-1)//2
    print(M)
    for n in range(1,N):
        for k in range(n+1,N):
            if n+k==N:
                continue
            print(n,k)
    for n in range(1,N):
        print(N,n)
else:
    M=N*(N-2)//2
    print(M)
    for n in range(1,N+1):
        for k in range(n+1,N+1):
            if n+k==N+1:
                continue
            print(n,k)
