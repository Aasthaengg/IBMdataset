from scipy.sparse.csgraph import floyd_warshall
from itertools import chain

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

d = floyd_warshall(C)

ans = sum(d[a][1] for a in chain(*A) if a != -1)

print(int(ans))