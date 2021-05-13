n,k=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x:x[0])
ans=float('inf')
for i in range(n-k+1):
    for j in range(i+k-1,n):
        x=l[j][0]-l[i][0]
        tl=sorted(l[i:j+1],key=lambda x:x[1])
        y=float('inf')
        for a in range(j-i+2-k):
            y=min(y,tl[a+k-1][1]-tl[a][1])
        ans=min(ans,x*y)
print(ans)