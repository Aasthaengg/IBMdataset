N,H,W=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
ans=0
for i in range(N):
    if H<=a[i][0] and W<=a[i][1] :
        ans+=1
    else :
        ans+=0
print(ans)