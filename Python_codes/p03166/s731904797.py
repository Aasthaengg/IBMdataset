from collections import deque
from collections import defaultdict
N, M = map(int, input().split())
d = [0]*N
G = defaultdict(list)
for i in range(M):
    s, t = map(int, input().split())
    d[t-1] += 1
    G[s-1].append(t-1)
q = deque([])
for i in range(N):
    if d[i] == 0:
        q.append(i)
ans = []
while q:
    s = q.popleft()
    ans.append(s)
    for t in G[s]:
        d[t] -= 1
        if d[t] == 0:
            q.append(t)
dp = [0] * (N+1)
num = 0
for i in range(0,N):
    for n in G[ans[i]]:
        dp[n] = max(dp[n], dp[ans[i]]+1)
print(dp[ans[-1]])