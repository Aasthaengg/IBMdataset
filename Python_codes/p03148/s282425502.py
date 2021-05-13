import sys
input=sys.stdin.readline

n,k=map(int,input().split())
sushi=[list(map(int,input().split())) for _ in range(n)]
sushi.sort(key=lambda x:x[1],reverse=True)

from collections import Counter
sel=Counter()
ans=0
sta=[]

for t,d in sushi[:k]:
    ans+=d
    sel[t]+=1
    sta.append([t,d])

ans+=len(sel)**2
tmp=ans
for t,d in sushi[k:]:
    if t in sel:continue
    while sta:
        tt,dd=sta.pop()
        if sel[tt]>1:
            tmp+=d-dd+2*len(sel)+1
            ans=max(ans,tmp)
            sel[tt]-=1
            sel[t]+=1
            break
print(ans)
