import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())

# ワーシャルフロイド
def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

# m行の入力から距離を値に持つ隣接行列を作成 0-indexed
# directed:無向グラフならFalse、有向グラフならTrue
def make_d_matrix(n,m,directed=False):
    inf = 10**13
    d = [[inf] * n for _ in range(n)]
    if(directed):
        for _ in range(m):
            a,b,c = map(int, input().split())
            d[a-1][b-1] = c
    else:
        for _ in range(m):
            a,b,c = map(int, input().split())
            d[a-1][b-1] = c
            d[b-1][a-1] = c
    return d

d = make_d_matrix(n,m)
d = warshall_floyd(d,n)

inf = 10**3
for i in range(n):
    for j in range(n):
        d[i][j] = 1 if (d[i][j] <= l) else inf

d = warshall_floyd(d,n)

q = int(input())

for _ in range(q):
    s,t = map(int, input().split())
    tmp = d[s-1][t-1]
    if(tmp >= inf):
        print(-1)
    else:
        print(tmp-1)