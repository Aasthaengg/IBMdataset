N=int(input())
A=[[] for i in range(0,N)]
for i in range(0,N):
    A[i]=list(map(int,input().split()))

count=0
for i in range(0,N):
    for j in range(0,N):
        for k in range(0,N):
            if A[i][j]>A[i][k]+A[k][j]:
                print(-1)
                exit()
            elif A[i][j]==A[i][k]+A[k][j] and k!=i and k!=j:
                break
        else:
            count+=A[i][j]

print(count//2)