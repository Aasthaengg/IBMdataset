W,H,N=map(int,input().split())
m=[[0]*W for i in range(H)]
ans=W*H

def c(a,b):
    global ans
    if m[a][b]==0:
        m[a][b]=1
        ans-=1
for i in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        for j in range(H):
            for k in range(x): c(j,k)
    if a==2:
        for j in range(H):
            for k in range(x,W): c(j,k)
    if a==3:
        for j in range(y):
            for k in range(W): c(j,k)
    if a==4:
        for j in range(y,H):
            for k in range(W):c(j,k)
print(ans)