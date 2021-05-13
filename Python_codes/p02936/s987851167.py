n,q=map(int, input().split())
go_list=[[] for i in range(n+1)]
cnt=[0]*(n+1)
Oya=[False]*(n+1)
Oya[1]=True
for i in range(n-1):
    a,b=map(int, input().split())
    go_list[a].append(b)
    go_list[b].append(a)

for i in range(q):
    p,x=map(int, input().split())
    cnt[p]+=x

from collections import deque
que=deque()

que.append(1)
sumi=[False]*(n+1)
sumi[1]=True
while que:
    ne=que.popleft()
    for i in go_list[ne]:
        if not sumi[i]:
            cnt[i]+=cnt[ne]
            sumi[i]=True
            que.append(i)

cnt.pop(0)
print(*cnt)
