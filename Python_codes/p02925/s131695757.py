n = int(input())
from collections import defaultdict
link = defaultdict(list)
inc = defaultdict(int)
chg=10**6
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(len(tmp)-1):
        me1 = min(i,tmp[j]-1)
        opp1 = max(i,tmp[j]-1)
        me2 = min(i,tmp[j+1]-1)
        opp2 = max(i,tmp[j+1]-1)
        now = me1*chg+opp1
        nxt = me2*chg+opp2
        link[now].append(nxt)
        inc[nxt]+=1

s=[]
for i in range(n):
    for j in range(i+1,n):
        if inc[i*chg+j]==0:
            s.append(i*chg+j)
res=[]
while s:
    nxt=s.pop()
    res.append(nxt)
    for m in link[nxt]:
        inc[m]-=1
        if inc[m]==0:
            s.append(m)
if len(res)!=((n-1)*n)//2:
    print(-1)
    exit()

path=defaultdict(lambda: -1)
for now in res:
    if path[now]==-1:
        path[now]=0
    for nxt in link[now]:
        path[nxt] = max(path[nxt],path[now]+1)
print(max(path.values())+1)