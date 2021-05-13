n,m = map(int,input().split())   #n=部屋 m=通路
adj = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

from collections import deque
q = deque()

dis = [-1] * n
ans = [0] * n

q.append(0)
while len(q) != 0:
    now = q.popleft()
    for to in adj[now]:
        if dis[to] != -1:
            continue
        dis[to] = dis[now] + 1
        q.append(to)
        ans[to] = now
print("Yes")
for i in range(1,n):
    print(ans[i] + 1)