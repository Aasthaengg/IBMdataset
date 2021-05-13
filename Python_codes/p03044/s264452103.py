from collections import deque
N=int(input())
lst=[[] for i in range(N)]
for i in range(N-1):
    U,V,W=map(int,input().split())
    lst[U-1].append([U-1,V-1,W])
    lst[V-1].append([V-1,U-1,W])

ans_lst=[-1]*N
queue=deque([])
for i in lst[0]:
    queue.append(i)
ans_lst[0]=0
while queue:
    u,v,w=queue.popleft()
    if ans_lst[v]==-1:
        ans_lst[v]=(ans_lst[u]+w)%2
        for i in lst[v]:
            queue.append(i)

for i in ans_lst:
    print(i)