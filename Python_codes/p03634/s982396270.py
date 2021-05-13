from collections import deque

N = int(input())
edges = [[]for _ in range(N+1)]
for i in range(N-1):
    a,b,c = map(int,input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))
dp = [0]*(N+1)

Q,K = map(int,input().split())
que = deque()
que.append((K,0))
path = {}
while que:
    now,cost = que.pop()
    path[now] = ""
    dp[now] = cost
    for x,c in edges[now]:
        if x not in path:
            que.append((x,cost+c))

for _ in range(Q):
    x,y = map(int,input().split())
    print(dp[x]+dp[y])
