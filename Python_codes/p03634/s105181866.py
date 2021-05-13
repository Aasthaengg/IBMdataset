from collections import deque
n = int(input())
tree = [[]*(n+1) for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
q,k = map(int,input().split())
parent = [-1]*(n+1)
distance = [-1]*(n+1)
distance[k] = 0
d = deque()
d.append(k)
while d:
    x = d.popleft()
    for child,length in tree[x]:
        if parent[x] == child:
            continue
        parent[child] = x
        distance[child] = distance[x] + length
        d.append(child)
for i in range(q):
    x,y = map(int,input().split())
    print(distance[x]+distance[y])
