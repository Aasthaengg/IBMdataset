n,m=map(int,input().split())

M=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    M.append([a,b])
M.sort()
#print(M)

ans=0
nL=M[0][0]
nR=M[0][1]
for i in range(m):
    L=M[i][0]
    R=M[i][1]
    if nR<=L:
        ans+=1
        nL=L
        nR=R
    else:
        nL=L
        nR=min(nR,R)
ans+=1
print(ans)