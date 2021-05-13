from copy import deepcopy

def warshall_floyd(n,a):
    d = deepcopy(a)
    is_via = [[False] * n for _ in range(n)]
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # 経由する場合
                if (d[i][k] != 0 and d[k][j] != 0) and (d[i][j] == d[i][k] + d[k][j]):
                    is_via[i][j] = True
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    flag = a == d
    return flag, is_via

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

flag, is_via = warshall_floyd(N,A)

if not flag:
    print(-1)
    exit()

ans = 0
for i in range(N):
    for j in range(i,N):
        if is_via[i][j]:
            continue
        ans += A[i][j]

print(ans)