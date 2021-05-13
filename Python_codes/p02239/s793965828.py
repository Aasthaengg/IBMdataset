from collections import deque
n=int(input())
v=[[] for _ in range(n)]
dist=[n+1]*n
dist[0]=0
for i in range(n):
    l=list(map(int,input().split()))
    if l[1]==0:
        continue
    else:
        for j in l[2:]:
            v[l[0]-1].append(j-1)

flg=1
q=deque()
while flg==1:
    flg=0
    q=deque()
    for i in range(n):
        q.append(i)
        chk=[0]*n
        while q:
            x=q.popleft()
            chk[x]=1
            d=dist[x]
            for j in v[x]:
                if chk[j]==1:
                    continue
                else:
                    if dist[j]>d+1:
                        flg=1
                        dist[j]=d+1
                        q.append(j)

for i in range(n):
    if dist[i]==n+1:
        print(i+1,-1)
    else:
        print(i+1,dist[i])
