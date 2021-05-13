n = int(input())

dl = [list(map(int,input().split())) for _ in range(n)]

# d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d  # d[i][j]に頂点i, j間の最短距離を格納
from copy import deepcopy
d = warshall_floyd(deepcopy(dl), n)

if d != dl:
    print(-1)
    exit()

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        flag = True
        for k in range(n):
            if i == k or k == j:
                continue
            if d[i][j] == d[i][k] + d[k][j]:
                flag = False
        if flag:
            ans += d[i][j]
print(ans//2)

