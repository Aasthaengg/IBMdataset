import sys

N=int(input())
ab=[list(map(int,input().split())) for i in range(N-1)]
c=list(map(int,input().split()))
c.sort(reverse=True)
data=[[] for i in range(N+1)]
for a,b in ab:
    data[a].append(b)
    data[b].append(a)
    
flag=[0]*(N+1)
ans=[0]*(N+1)
flag[1]=1
k=0
que=[1]
while que:
    for u in que:
        ans[u]=c[k]
        k+=1
    if k>N:
        break
    h=[]
    for u in que:
        for v in data[u]:
            if flag[v]==0:
                flag[v]=1
                h.append(v)
    que=h
print(sum(ans[2:]))
print(*ans[1:])