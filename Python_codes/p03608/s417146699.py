from itertools import permutations
N, M, R = map(int, input().split())

# ワーシャフロイドで全点の最短経路を求める
# 訪問順を全列挙して全て試して、最も短いものが答えになる
# 計算量はワーシャルフロイドで200**3、全列挙で8!(40320)
# ワーシャルフロイドが間に合えばいけそう

r = list(map(lambda x: int(x)-1, input().split()))
edge = [[10**9] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edge[a][b] = c
    edge[b][a] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])
    
#print(edge)
ans = 10 ** 20
for per in permutations(r):
    tmp = 0
    for i in range(R-1):
        tmp += edge[per[i]][per[i+1]]
    ans = min(ans, tmp)

print(ans)