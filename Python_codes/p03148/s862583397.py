N,K=map(int, input().split())
td=[list(map(int,input().split())) for i in range(N)]
best=[0]*(N+1)
other=[]
from heapq import heappop,heappush
td.sort(key=lambda x: x[1],reverse=True)
shurui=0
for i in range(K):
    if best[td[i][0]]==0:
        best[td[i][0]]=td[i][1]
        shurui+=1
    elif best[td[i][0]]<td[i][1]:
        heappush(other,best[td[i][0]])
        best[td[i][0]]=td[i][1]
    else:
        heappush(other,td[i][1])

sumbest=sum(best)
sumother=sum(other)
ans=sumbest+sumother+shurui**2

for i in range(K,N):
    if best[td[i][0]]==0 and len(other)>0:
        best[td[i][0]]=td[i][1]
        shurui+=1
        sumbest+=td[i][1]
        sumother-=heappop(other)
        ans=max(ans,sumbest+sumother+shurui**2)

print(ans)
