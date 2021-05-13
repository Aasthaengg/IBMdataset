from collections import deque
n = int(input())
route = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    route[a].append((b,c))
    route[b].append((a,c))
q,k = map(int,input().split())
ans = [-1 for i in range(n+1)]
ans[k] = 0
d = deque()
d.append((k,0))
while d:
    now,cost = d.popleft()
    for i , j in route[now]:
        if ans[i] == -1:
            ans[i] = cost+j
            d.append((i,cost+j))
for i in range(q):
    x,y = map(int,input().split())
    print(ans[x]+ans[y])