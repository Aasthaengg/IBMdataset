N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    if A[i][i] != 0:
        print(-1)
        exit()
import copy
ca = copy.deepcopy(A)

for k in range(N):
    for i in range(N):
        for j in range(N):
            ca[i][j] = min(ca[i][j],ca[i][k] + ca[k][j])


## 各頂点間に最短距離通りの辺を引いた時に最短距離が更新されていたらそれはどうやったって構築できない
for i in range(N):
    for j in range(N):
        if A[i][j] != ca[i][j]:
            print(-1)
            exit()

ans = 0
for i in range(N):
    for j in range(N):
        need = True
        for k in range(N):
            if i != k and j != k and ca[i][k] + ca[k][j] == ca[i][j]: # ijのパスが無くても制約を満たせるならijのパスは消して良い
                need = False
        if need:
            ans += ca[i][j]
ans = ans//2 # 各パスを2回ずつ数えている
print(ans)