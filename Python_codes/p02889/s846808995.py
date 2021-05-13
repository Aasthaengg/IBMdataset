# ワ―シャルフロイドで解くよ
def main():
    import sys
    input = sys.stdin.readline  # 1行ごとの入力を繰り返し扱う場合の高速化
    N, M, L = map(int, input().split())
    # distanceを格納(未到達は無限遠として初期化)
    d = [[10 ** 12] * N for _ in range(N)]  
    # input-edges
    for i in range(M):
        a, b, c = map(int, input().split())
        if L >= c: # 距離がLより大きいのは無視
            d[a - 1][b - 1] = d[b - 1][a - 1] = c
    for i in range(N):
        d[i][i] = 0  # 自己ループ無
    
    # ワ―シャルフロイド法適用
    # 町間の最短距離を一度求める。
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][k] + d[k][j], d[i][j])
    
    # 先ほど求めた町間の内、最短距離がL以下のものを距離1で結ぶ。
    edge = [[10 ** 12] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if d[i][j] <= L:
                edge[i][j] = 1
    
    # もう一度ワ―シャルフロイド法適用
    for k in range(N):
        for i in range(N):
            for j in range(N):
                edge[i][j] = min(edge[i][k] + edge[k][j], edge[i][j])
    
    # input-query
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        if edge[s - 1][t - 1] >= 10 ** 12:
            print(-1)
        else:
            print(edge[s - 1][t - 1] - 1)  # 最初に燃料Lがある分、マイナス1をする。
    
if __name__ == "__main__":
    main()