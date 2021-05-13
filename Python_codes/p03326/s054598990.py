N,M=map(int,input().split())
cake=[list(map(int,input().split())) for _ in range(N)]
ans=0
for i in range(1<<3):
    point=[0]*N
    for j in range(N):
        for k in range(3):
            point[j]+=(-1+(i>>k & 1)*2)*cake[j][k]
    point.sort()
    ans=max(ans,sum(point[-M:]))
    if M==0:
        ans=0
print(ans)
