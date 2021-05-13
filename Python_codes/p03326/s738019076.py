n,m=map(int,input().split())
A=[]
for i in range(n):
    x,y,z=map(int,input().split())
    A.append([x,y,z])
    
F=[[1,1,1],[1,1,-1],[1,-1,1],[-1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
ans=0
for f in F:
    C=[]
    for i in range(n):
        s=f[0]*A[i][0]+f[1]*A[i][1]+f[2]*A[i][2]
        C.append([s,i])
    C=list(reversed(sorted(C)))
    cnt=[0,0,0]
    for i in range(m):
        a=C[i][1]
        for i in range(3):
            cnt[i]+=A[a][i]
    ans=max(abs(cnt[0])+abs(cnt[1])+abs(cnt[2]),ans)
print(ans)