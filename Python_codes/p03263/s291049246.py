H,W=map(int,input().split())
a=[[] for i in range(0,H)]
for i in range(0,H):
    a[i]=list(map(int,input().split()))

ans=[]
for i in range(0,H):
    for j in range(0,W-1):
        if a[i][j]%2==1:
            ans.append((i,j,i,j+1))
            a[i][j+1]+=1

for i in range(0,H-1):
    if a[i][W-1]%2==1:
        ans.append((i,W-1,i+1,W-1))
        a[i+1][W-1]+=1

N=len(ans)
print(N)
for i in range(0,N):
    x,y,z,w=ans[i]
    print(x+1,y+1,z+1,w+1)