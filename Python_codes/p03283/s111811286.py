n, m, q = map(int, input().split())

train = [[0 for _ in range(n+1)] for __ in range(n+1)]

for _ in range(m):
    l, r = map(int, input().split())
    train[l][r] += 1

ans = [[0 for _ in range(n+1)] for __ in range(n+1)]

for i in range(n):
    for j in range(n+1):
        ans[i+1][j] = ans[i][j] + train[i+1][j]

for j in range(n):
    for i in range(n+1):
        ans[i][j+1] = ans[i][j+1] + ans[i][j]

for __ in range(q):
    p, q = map(int, input().split())
    print(ans[q][q] - ans[q][p-1] - ans[p-1][q] + ans[p-1][p-1])