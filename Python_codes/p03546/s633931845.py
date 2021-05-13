import copy

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)] 

INF = 10 ** 6
d = copy.deepcopy(c)
for k in range(10):
    for i in range(10):
        for j in range(10):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

res = 0
for arr in A:
    for a in arr:
        if a == -1:
            continue
        else:
            res += d[a][1]

print(res)