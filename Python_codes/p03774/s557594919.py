N,M=map(int,input().split())

ab=[list(map(int,input().split())) for i in range(N)]
cd=[list(map(int,input().split())) for i in range(M)]

ans=[0 for i in range(N)]
for i in range(N):
    dis=10**9
    for j in range(M):
        xx=abs(ab[i][0]-cd[j][0])
        yy=abs(ab[i][1]-cd[j][1])
        temp=xx+yy
        if dis>temp:
            dis=temp
            ans[i]=j
for a in ans:
    print(a+1)