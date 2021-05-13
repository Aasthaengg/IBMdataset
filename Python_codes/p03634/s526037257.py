from queue import deque

n = int(input())
li = [[] for _ in range(n)]
length = {}
length_path = [0]*n

for i in range(n-1):
    u,v,w = map(int,input().split())
    u,v = u-1,v-1
    if u < v:
        length[(u,v)] = w
    else:
        length[(v,u)] = w
    li[u].append(v)
    li[v].append(u)

q,k = map(int,input().split())
k -= 1

work_queue = deque([])
visited = [False]*n

work_queue.append(k)

while work_queue:
    now = work_queue.popleft()
    visited[now] = True
    for i in li[now]:
        if visited[i]:
            continue
        work_queue.append(i)
        visited[i] = True
        if now < i:
            length_path[i] = length_path[now]+length[(now,i)]
        else:
            length_path[i] = length_path[now]+length[(i,now)]

for i in range(q):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    print(length_path[x]+length_path[y])