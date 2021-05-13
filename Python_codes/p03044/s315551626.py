from collections import deque
N = int(input())
E = [[] for i in range(N + 1)]
ans = [-1]*(N+1)
ans[1] = 0
for i in range(N - 1):
    u, v, w = map(int, input().split((' ')))
    E[u].append((u, v, w % 2))
    E[v].append((v, u, w % 2))
dfs = deque(E[1])
while dfs:
    p = (dfs.popleft())
    f, t, w = p
    if ans[t] != -1:
        continue
    if w == 0:
        ans[t] = ans[f]
    else:
        ans[t] = 0 if ans[f] else 1
    for i in E[t]:
        dfs.append(i)
for i in ans[1:]:
    print(i)