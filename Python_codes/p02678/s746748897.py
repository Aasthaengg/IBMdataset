from collections import deque
n,m=map(int,input().split())
A=[[] for i in range(n)]
for i in range(m) :
    a,b=map(int,input().split())
    A[b-1].append(a-1)
    A[a-1].append(b-1)
depth=[-1]*n
visit=deque([0])

while True :
    if len(visit)==0 :
        break
    x=visit.popleft()
    for i in A[x] :
        if depth[i]==-1 :
            depth[i]=x+1
            visit.append(i)

print("Yes")
[print(i) for i in depth[1:]]
