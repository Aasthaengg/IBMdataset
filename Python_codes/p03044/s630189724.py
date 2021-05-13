from collections import deque
n = int(input())
route = [[] for i in range(n+1)]
for i in range(n-1):
    u , v , w = map(int,input().split())
    route[u].append((v,w))
    route[v].append((u,w))

ans = [-1 for i in range(n+1)]

d = deque()
d.append(1)
ans[1] = 0
while d:
    now = d.popleft()
    for i , j in route[now]:
        if ans[i] == -1:
            if j % 2 == 0:
                ans[i] = ans[now]
            elif j % 2 == 1:
                ans[i] = (ans[now]+1)%2
            d.append(i)

for i in range(1,n+1):
    print(ans[i])