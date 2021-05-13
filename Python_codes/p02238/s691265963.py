def dfs(v, k):
    if ans[v][1] == 0:
        ans[v][1] = k
    else:
        return k - 1
    for i in d[v]:
        k = dfs(i, k + 1)
    k += 1
    if ans[v][2] == 0:
        ans[v][2] = k
    return k


G = int(input())
vlst = [list(map(int, input().split())) for _ in range(G)]
d = [[] for _ in range(G)]
for i in range(G):
    for j in range(vlst[i][1]):
        d[i].append(vlst[i][2 + j] - 1)
ans = [[_, 0, 0] for _ in range(G)]
k = 1
for i in range(G):
    k = dfs(i, k) + 1
for i in ans:
    print(i[0] + 1, i[1], i[2])
