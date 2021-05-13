from collections import*
n=int(input())
l=[[]for i in range(n)]
ans=[-1 for i in range(n)]
visit=[False for i in range(n)]
ans[0]=0
for i in range(n-1):
    u,v,w=map(int,input().split())
    l[u-1].append((v-1,w))
    l[v-1].append((u-1,w))
      
q=deque()
q.append((0,0,-1))
while q:
    v,d,p=q.popleft()
    if d%2==0:
        ans[v]=0
    else:
        ans[v]=1
    for u,w in l[v]:
        if u==p:
            continue
        q.append((u,d+w,v))
print('\n'.join(map(str, ans)))