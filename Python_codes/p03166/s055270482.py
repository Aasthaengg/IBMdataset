from collections import deque
n,m = map(int,input().split())
path = [set() for _ in range(n)]
to = [0]*n
dp = [0]*n
for _ in range(m):
    x,y = map(int,input().split())
    path[x-1].add(y-1)
    to[y-1] += 1

que = deque()
for i in range(n):
    if to[i] == 0:
        que.append(i)
ans = 0
while que:
    p = que.popleft()
    for i in path[p]:
        to[i] -= 1
        if to[i] == 0:
            que.append(i)
        dp[i] = max(dp[i], dp[p] + 1)
        ans = max(ans, dp[i])
print(ans)
