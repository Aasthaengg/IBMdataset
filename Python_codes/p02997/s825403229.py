# ABC 131 E

N,K=map(int,input().split())

M=(N-1)*(N-2)//2
if K<=M:
    # OK
    print(N-1+M-K)
    for i in range(1,N):
        print(i,N)
    i,j=1,2
    for _ in range(M-K):
        print(i,j)
        j+=1
        if j==N:
            i+=1
            j=i+1
else:
    # NG
    print(-1)