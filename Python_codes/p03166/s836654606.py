import collections
n,m = map(int,input().split())
d = {}
indegree = [0]*n
for _ in range(m):
    x,y = map(int,input().split())
    d[x-1] = d.get(x-1,[]) + [y-1]
    indegree[y-1] += 1
dp = [0]*n
q = collections.deque([i for i in range(n) if indegree[i] == 0])
while q:
    node = q.popleft()
    for nei in d.get(node,[]):
        indegree[nei] -= 1
        dp[nei] = max(dp[nei],dp[node]+1)
        if indegree[nei] == 0:
            q.append(nei)
print(max(dp))