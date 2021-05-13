N=int(input())
if N%2:
    print(N*(N-2)//2+1)
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i+j!=N:
                print(i,j)
else:
    print(N*(N-2)//2)
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i+j!=N+1:
                print(i,j)