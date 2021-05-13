import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]
mn = [[int(1e9) for j in range(10)] for i in range(10)]

def dfs(s, n, d):
    if n == 1:
        mn[s][n] = min(mn[s][n], d)
    else:
        if mn[s][n] <= d:
            return
        mn[s][n] = min(mn[s][n], d)
        for i in range(10):
            dfs(s, i, d+c[n][i])


for i in range(10):
    dfs(i, i, 0)

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1:
            continue
        ans += mn[A[i][j]][1]

print(ans)
