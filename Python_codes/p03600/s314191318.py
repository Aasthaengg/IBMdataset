import copy

def warshal_floyd(d):
    # d[i][j] := iからjへの最短距離
    global N
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    # "今現在求まっているiからjへの最短距離"と"今現在求まっているiからkへの最短距離 + 今現在求まっているkからjへの最短距離 の和"を比較する
    return d


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
graph = copy.deepcopy(A)
# for a in A:
#     print(a)
# 余分な辺を消去する問題
A = warshal_floyd(A)
for i in range(N):
    for j in range(N):
        if A[i][j] != graph[i][j]:
            print(-1)
            exit()

# 最短経路であることは分かった
flag = [[True]*N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == graph[i][k] + graph[k][j] and i != k and k != j:
                flag[i][j] = False

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if flag[i][j] == True:
            ans += graph[i][j]
print(int(ans))
