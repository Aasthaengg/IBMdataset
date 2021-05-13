n,ma,mb=map(int,input().split())
ab=[[[10**6]*401 for _ in range(401)] for _ in range(n+1)]
ab[0][0][0]=0

for p in range(1,n+1):
    a,b,c=map(int,input().split())
    for i in range(400):
        for j in range(400):
            ab[p][i][j]=min(ab[p][i][j],ab[p-1][i][j])
            if i+a<=400 and j+b<=400:
                ab[p][i+a][j+b]=min(ab[p][i+a][j+b],ab[p-1][i][j]+c)

ans=10**6-1
for i in range(401):
    for j in range(401):
        if i!=0 and j!=0:
            if i*mb==j*ma:
                ans=min(ans,ab[n][i][j])

if ans==10**6-1:
    print(-1)
else:
    print(ans)