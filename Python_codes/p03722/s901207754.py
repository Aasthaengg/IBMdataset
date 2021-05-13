n,m=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]

inf=float("inf")
data=[-inf]*(n+1)
data[1]=0
for i in range(n):
    for a,b,c in abc:
        if data[a]!=inf:
            data[b]=max(data[b],data[a]+c)

lst=data[:]
for i in range(n):
    for a,b,c in abc:
        if data[a]!=inf:
            data[b]=max(data[b],data[a]+c)

que=[]
for i in range(1,n+1):
    if lst[i]!=data[i]:
        que.append(i)
        
flag=[0]*(n+1)
for u in que:
    flag[u]=1

li=[[] for i in range(n+1)]
for a,b,c in abc:
    li[a].append(b)

while que:
    h=que.pop()
    for u in li[h]:
        if flag[u]==0:
            flag[u]=1
            que.append(u)

if flag[n]==1:
    print("inf")
else:
    print(data[n])