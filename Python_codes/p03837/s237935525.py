inf = 10 ** 18
n, m = map(int, input().split())
d = [[inf for _ in range(n)] for _ in range(n)]
edge = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(n):
    d[i][i] = 0
for a, b, c in edge:
    d[a-1][b-1] = c
    d[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for a, b, c in edge:
    if d[a-1][b-1] != c:
        ans += 1
print(ans)