from collections import deque
print("Yes")

N,M=map(int,input().split())
lst=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    lst[a-1].append(b-1)
    lst[b-1].append(a-1)
q=deque(lst[0])
go=[None]*N
for i in lst[0]:
    go[i]=0
while q:
    v=q.popleft()
    for new in lst[v]:
        if go[new]==None:
            go[new]=v
            q.append(new)
for i in go[1:]:
    print(i+1)