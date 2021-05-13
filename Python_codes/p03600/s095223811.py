N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
res=0
flag=[[False]*N for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j]>A[i][k]+A[k][j]:
                print(-1)
                exit()
            elif k!=i and k!=j and A[i][j]==A[i][k]+A[k][j] and not flag[i][j] and not flag[j][i]:
                flag[i][j]=True
                flag[j][i]=True
                res-=A[i][j]
ans=sum(sum(A[i]) for i in range(N))//2+res

print(ans)