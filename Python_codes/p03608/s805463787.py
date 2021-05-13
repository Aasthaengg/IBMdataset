from itertools import permutations as perm

n, m, r = map(int, input().split())
r = list(map(lambda x: int(x) - 1, input().split()))
d = [[10 ** 10] * n for _ in range(n)]
for i in range(m):
    abc = tuple(map(int, input().split()))
    a = abc[0] - 1
    b = abc[1] - 1
    c = abc[2]
    d[a][b] = c
    d[b][a] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            d[j][i] = d[i][j]

ans = 10 ** 10
for arr in perm(r):
    rep = 0
    for i in range(len(arr) - 1):
        rep += d[arr[i]][arr[i + 1]]
    ans = min(ans, rep)
print(ans)
