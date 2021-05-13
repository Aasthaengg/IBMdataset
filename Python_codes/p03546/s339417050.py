from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense

# 入力
H, W = map(int, input().split())
G = [[int(i) for i in input().split()] for j in range(10)]
G = csgraph_from_dense(G)

dist = floyd_warshall(G)
ans = 0
for h in range(H):
    line = [int(i) for i in input().split()]
    for w in range(W):
        if line[w] == -1:
            continue
        ans += dist[line[w]][1].astype(int)

print(ans)