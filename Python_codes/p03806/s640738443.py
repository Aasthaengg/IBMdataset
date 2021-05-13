N,Ma,Mb=map(int,input().split())
medic=[tuple(map(int,input().split())) for i in range(N)]
from collections import defaultdict
dp=defaultdict(lambda : float('inf'))
dp[(0,0)]=0
for a,b,c in medic:
    dpc=dp.copy()
    for k,v in dpc.items():
        x,y=k
        dp[(x+a,y+b)]=min(dp[(x+a,y+b)],v+c)
ans=10**10
for i in range(1,1+N):
    ans=min(ans,dp[(Ma*i,Mb*i)])
if ans>10**9:
    print(-1)
else:
    print(ans)