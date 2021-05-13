def dfs(i, cnt):
    D[i] = cnt
    cnt += 1
    for c in v[i]:
        if D[c-1] == -1:
            cnt = dfs(c-1, cnt)
    F[i] = cnt
    cnt += 1
    return cnt


N = int(input())
g = [0]*N
k = [0]*N
v = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    g[i] = tmp[0]
    k[i] = tmp[1]
    if k[i] != 0:
        v[i] = sorted(tmp[2:])

D = [-1] * N
F = [-1] * N
cnt = 1
for i in range(N):
    if D[i] == -1:
        cnt = dfs(i, cnt)

for i, (d, f) in enumerate(zip(D, F)):
    print(i+1, d, f)

