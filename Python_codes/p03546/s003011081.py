H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)] 

INF = 10 ** 6
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

res = 0
for arr in A:
    for a in arr:
        if a == -1:
            continue
        else:
            res += c[a][1]

print(res)