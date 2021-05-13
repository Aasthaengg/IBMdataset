n=int(input())

L=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    L[a].append(b)
    L[b].append(a)

fe=[0 for i in range(n+1)]
que=[(1,0)]
visited=[0 for i in range(n+1)]
visited[1]=1
head=0

while len(que)>head:
    now=que[head]
    head+=1
    fe[now[0]]=now[1]
    for nex in L[now[0]]:
        if visited[nex]==0:
            visited[nex]=1
            que.append((nex,now[1]+1))
            
sn=[0 for i in range(n+1)]
que=[(n,0)]
visited=[0 for i in range(n+1)]
visited[-1]=1
head=0

while len(que)>head:
    now=que[head]
    head+=1
    sn[now[0]]=now[1]
    for nex in L[now[0]]:
        if visited[nex]==0:
            visited[nex]=1
            que.append((nex,now[1]+1))

kaname=[]
for i in range(1,n+1):
    ck=fe[i]-sn[i]
    if ck==1 or ck==2:
        kaname.append(i)

cnt=0
que=[(1,0)]
visited=[0 for i in range(n+1)]
visited[1]=1
head=0

while len(que)>head:
    now=que[head]
    head+=1
    cnt+=1
    for nex in L[now[0]]:
        if visited[nex]==0 and not nex in kaname:
            visited[nex]=1
            que.append((nex,now[1]+1))

if cnt*2>n:
    print("Fennec")
else:
    print("Snuke")