N=int(input())

if N%2:
    print(N*(N-1)//2-N//2)
    for i in range(1,N+1):
        for j in range(1,i):
            if i+j==N:
                continue
            print(i,j)
else:
    print(N*(N-1)//2-N//2)
    for i in range(1,N+1):
        for j in range(1,i):
            if i+j==N+1:
                continue
            print(i,j)