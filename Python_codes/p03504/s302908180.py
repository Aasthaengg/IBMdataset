from itertools import accumulate

N,C=map(int,input().split())
imos=[0 for i in range(0,10**5+2)]
bangumi={i:[] for i in range(1,C+1)}
for i in range(0,N):
    s,t,c=map(int,input().split())
    imos[s]+=1
    imos[t+1]+=-1
    bangumi[c].append((s,t))

ans=list(accumulate(imos))
for i in range(1,C+1):
    bangumi[i].sort()

for i in range(1,C+1):
    if len(bangumi[i])>1:
        for j in range(0,len(bangumi[i])-1):
            s,t=bangumi[i][j]
            u,v=bangumi[i][j+1]
            if t==u:
                ans[t]-=1

print(max(ans))