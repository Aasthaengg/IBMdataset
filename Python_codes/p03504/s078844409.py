N,C=map(int,input().split())
from collections import defaultdict
Cbef=defaultdict(int)
time=defaultdict(int)
TV=[tuple(map(int,input().split())) for i in range(N)]
TV.sort(key=lambda x:x[0])
for s,t,c in TV:
    if Cbef[c]==s:
        time[s]+=1
        time[t]-=1
        Cbef[c]=t
    else:
        time[s-1]+=1
        time[t]-=1
        Cbef[c]=t
ans=0
now=time[0]
ans=now
for i in range(1,10**5+1):
    now+=time[i]
    ans=max(ans,now)
print(ans)