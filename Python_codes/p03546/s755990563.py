h,w = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(10)]
a = [list(map(int,input().split())) for _ in range(h)]
INF = 10**10
d = [[c[i][j] for j in range(10)] for i in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += d[a[i][j]][1]
print(ans)