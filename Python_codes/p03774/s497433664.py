N,M=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(N)]
cd=[list(map(int,input().split())) for _ in range(M)]

for i in range(N):
    d=float("inf")
    ans=-1
    for j in range(M):
        if d>abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1]):
            d=abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
            ans=j+1
    print(ans)