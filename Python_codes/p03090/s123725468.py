N=int(input())
if N%2==1:
    hen=[]
    for i in range(1,N):
        for j in range(i+1,N+1):
            if i+j!=N:
                hen.append([i,j])

    M=len(hen)
    print(M)
    for i in range(0,M):
        print(*hen[i])

else:
    hen=[]
    for i in range(1,N):
        for j in range(i+1,N+1):
            if i+j!=N+1:
                hen.append([i,j])

    M=len(hen)
    print(M)
    for i in range(0,M):
        print(*hen[i])