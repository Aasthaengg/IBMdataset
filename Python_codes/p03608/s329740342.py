"""ABC073D joisino's travel
"""
from itertools import permutations
N,M,R=map(int, input().split())
r = list(map(lambda x: int(x)-1, input().split()))
INF = float("inf")
D = [[INF]*(N) for _ in range(N)]
for _ in range(M):
    a,b,c=map(int, input().split())
    D[a-1][b-1]=c
    D[b-1][a-1]=c
    
def warshall_floyd(adj_mat: list):
    """
    ワーシャルフロイド
    隣接行列を受け取る(隣接していないノードはINF、自身へのコストは0)
    全点の間の最短距離をあらわす行列を返す(V * V)
    O(|V|**3)
    ネスト深くならないバージョン
    """
    V = len(adj_mat)
    for k in range(V): # 経由点
        for i in range(V): # 出発点
            for j in range(V): # 終点
                adj_mat[i][j] = min(
                    adj_mat[i][j],
                    adj_mat[i][k] + adj_mat[k][j]
                )
    return adj_mat
D = warshall_floyd(D)
ans = INF
for tpl in permutations(r, len(r)):
    tmp = 0
    for i in range(len(tpl)-1):
        tmp += D[tpl[i]][tpl[i+1]]
    ans = min(ans, tmp)
print(ans)