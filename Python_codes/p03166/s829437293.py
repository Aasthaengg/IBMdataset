n, m = map(int, input().split())
G = [[] for i in range(n)]
enter = [0] * n
for i in range(m):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    enter[y-1] += 1

dp = [0] * n
s = []
for i in range(n):
    if not enter[i]:
        s.append(i)

while(s!=[]):
    v = s.pop(0)
    for i in G[v]:
        enter[i] -= 1
        if not enter[i]:
            s.append(i)
            dp[i] = dp[v]+1

print(max(dp))