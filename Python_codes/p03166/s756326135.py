N, M = map(int, input().split())

G = [[] for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)

inord = [0 for i in range(N)]
stack = []
for u in range(N):
    for v in G[u]:
        inord[v] += 1

for i in range(N):
    if inord[i] == 0:
        stack.append(i)

ans = []
while len(stack):
    u = stack.pop()
    ans.append(u)
    for v in G[u]:
        inord[v] -= 1
        if inord[v] == 0:
            stack.append(v)

#ansはtopological_sortされている

#dp[i]:i番目にたどり着くまでの最長経路
dp = [0 for i in range(N)]
for u in ans:
    for v in G[u]:
        dp[v] = max(dp[u]+1, dp[v])

ret = 0
for i in range(N):
    ret = max(ret, dp[i])
print(ret)