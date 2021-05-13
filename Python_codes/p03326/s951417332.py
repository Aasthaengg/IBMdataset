n,m=map(int,input().split())
XYZ=[list(map(int,input().split())) for _ in range(n)]

ans=0
for i in (-1,1):
    for j in (-1,1):
        for k in (-1,1):
            A=sorted([i*x+j*y+k*z for x,y,z in XYZ],reverse=True)
            ans=max(ans,sum(A[:m]))

print(ans)