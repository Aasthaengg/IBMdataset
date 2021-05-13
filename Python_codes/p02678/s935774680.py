from collections import deque

n,m = map(int,input().split())
aisle=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    aisle[a-1].append(b)
    aisle[b-1].append(a)

queue = deque([1])
visited = [-1] * n
parent = [0] * n
now = 1

visited[0]=0

while len(queue) > 0:
    now = queue.popleft()
    for i in aisle[now-1]:
        if visited[i-1]==-1:
            queue.append(i)
            visited[i-1]=visited[now-1]+1
            parent[i-1] = now


print('Yes')
for i in range(2,n+1):
    print(parent[i-1])
