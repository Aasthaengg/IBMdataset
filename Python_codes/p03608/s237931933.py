import sys
input = sys.stdin.readline

n,m,r= map(int, input().split())
rr= list(map(int, input().split()))
a= [list(map(int, input().split())) for i in range(m)]
d=[[float('inf')]*n for i in range(n)]
for i in range(n):
    d[i][i]=0

for i,j,k in a:
    i-=1
    j-=1
    d[i][j]=k
    d[j][i]=k


# ワーシャルフロイド　全点最短経路、負の距離あっても可　o(n**3)
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])

    return d
d=warshall_floyd(d)


# bit DP
# dp[S][v]: 訪れた点の集合がSで最後にVを訪れた時のVのMIN
INF=float('inf')
dp=[[INF]*r for i in range(1<<r)]
dp[0]=[0]*r

for i in range(1<<r):
    for k in range(r):
        # 訪問リストに入っているものを最後に訪問する時
        if (i >> k) & 1:
            if i^(1<<k)==0:
                dp[i][k]=0
            else:
                # 最後に訪れるものを除いた集合でどこを最後に訪問した時がminか調べる
                for l in range(r):
                    if (i ^ (1 << k))>>l:
                        dpm = dp[i ^ (1 << k)][l]
                        ad = d[rr[l] - 1][ rr[k] - 1]
                        dp[i][k] = min(dpm + ad, dp[i][k])

print(min(dp[-1]))