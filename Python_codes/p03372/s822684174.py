N,C=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]

cumR=[0]*(N+1)
cummaxR=[0]*(N+1)
for i in range(N):
    cumR[i+1]=cumR[i]+li[i][1]-li[i][0]
    cummaxR[i+1]=cummaxR[i]+li[i][1]-li[i][0]*2
    if i>0:
        cumR[i+1]+=li[i-1][0]
        cummaxR[i+1]+=li[i-1][0]*2
for i in range(1,N):
    cummaxR[i]=max(cummaxR[i],cummaxR[i-1])
cumL=[0]*(N+1)
cummaxL=[0]*(N+1)
for i in reversed(range(N)):
    cumL[i]=cumL[i+1]+li[i][1]-(C-li[i][0])
    cummaxL[i]=cummaxL[i+1]+li[i][1]-(C-li[i][0])*2
    if i<N-1:
        cumL[i]+=(C-li[i+1][0])
        cummaxL[i]+=(C-li[i+1][0])*2
for i in reversed(range(N)):
    cummaxL[i]=max(cummaxL[i],cummaxL[i+1])
ans=0
for i in range(N):
    ans=max(ans,cumR[i+1]+cummaxL[i+1])
    ans=max(ans,cumL[i]+cummaxR[i])
print(ans)