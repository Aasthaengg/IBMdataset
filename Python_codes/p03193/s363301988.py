N,H,W=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(N)]
c=0
for i in range(N):
    if (mat[i][0]>=H)and(mat[i][1]>=W):
        c=c+1
print(c)