from collections import deque

n,x,y=map(int,input().split())
map=[[] for _ in range(n+1)]
for i in range(1,n):
    map[i].append(i+1)
    map[i+1].append(i)
map[x].append(y)
map[y].append(x)

ans=[0]*n

for j in range(1,n+1):
    dict=[-1]*(n+1)
    que=deque()
    que.append(j)
    dict[j]=0
    while que:
        t=que.popleft()
        for k in map[t]:
            if dict[k]==-1:
                dict[k]=dict[t]+1
                que.append(k)
    for l in range(1,n+1):
        ans[dict[l]]+=1
for m in range(1,n):
    print(ans[m]//2)