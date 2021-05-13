N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
is_need = [[1]*N for i in range(N)]

def warshall_floyd(adj_mat: list):
    """
    ワーシャルフロイド
    隣接行列を受け取る(隣接していないノードはINF、自身へのコストは0)
    全点の間の最短距離をあらわす行列を返す(V * V)
    O(|V|**3)
    ネスト深くならないバージョン
    """
    mat = adj_mat.copy()
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    return -1
                elif mat[i][j] == mat[i][k] + mat[k][j] and i != k and k != j:
                    is_need[i][j] = 0
                
    return mat

adj = warshall_floyd(A)
if adj == -1:
    print(-1)
else:
    ans = 0
    for i in range(N):
        for j in range(N):
            if is_need[i][j]:
                ans += A[i][j]
    print(ans//2)