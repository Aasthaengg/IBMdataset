from collections import deque
N=int(input())
ab=list(list(map(int,input().split()))for _ in range(N-1))
c=list(map(int,input().split()))
c.sort(reverse=True)
graph=[[] for _ in range(N+1)]
for a,b in ab:
    graph[a].append(b)
    graph[b].append(a)
queue=deque([1])
ans=[[] for _ in range(N+1)]
sumans=-c[0]
c=deque(c)
while len(queue)>0:
    x=queue.popleft()
    y=c.popleft()
    ans[x].append(y)
    sumans+=y
    for i in graph[x]:
        if ans[i]==[]:
            queue.append(i)
print(sumans)
for j in ans[1:]:
    print(*j,end=' ')
