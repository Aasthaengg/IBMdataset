h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

cost = [[float("inf")]*10 for _ in range(10)]
#cost[k][i][j]はｋ個までの頂点を経由して、頂点iから頂点jへ行くときの最小コスト
#cost[0][i][j]は何も経由しないのでc_ijと等しい
#ｋのところは省略できる
for i in range(10):
    for j in range(10):
        cost[i][j] = c[i][j]


for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
#print(cost)
ans = 0
for i in range(h):
    for j in range(w):
        a_ij = a[i][j]
        if a_ij == -1 or a_ij == 1:
            continue
        ans += cost[a_ij][1]
print(ans)



