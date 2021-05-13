def BellmanFord(start):
    # グラフの初期化 始点を0それ以外をinf
    inf = float("inf")
    dist = [inf] * N
    dist[start] = 0
    
    for i in range(N):
        update = False
        for x, y, z in G:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                update = True
                
                # 負の閉路を検出
                if y == N - 1 and i == N - 1:
                    return "inf"

        if update is False:
            break
        
    return -dist[-1]

N, W = map(int, input().split())  # 頂点, 辺
G = []
for _ in range(W):
    x, y, z = map(int, input().split())  # start, end, cost
    x, y, z = x - 1, y - 1, -z
    G.append([x, y, z])
    # G.append([y, x, z]) # 無向グラフのときのみ

d = BellmanFord(0)
print(d)
