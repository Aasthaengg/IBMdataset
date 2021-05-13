from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

G = csgraph_from_dense(c)
d = floyd_warshall(G).astype(int)

ans = 0

for l in a:
    for ai in l:
        if ai == -1:
            continue
        ans += d[ai][1]

print(ans)


