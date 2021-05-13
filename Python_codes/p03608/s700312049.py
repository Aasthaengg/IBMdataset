import sys
import itertools

def warshall_floyd(d, n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

N, M, R = map(int, sys.stdin.readline().split())
r = list(map(int, sys.stdin.readline().split()))

# 全点間の距離
d = [[float("inf")]*N for i in range(N)] 
for _ in range(M):
	a, b, c = map(int, sys.stdin.readline().split())
	d[a-1][b-1] = c
	d[b-1][a-1] = c

d = warshall_floyd(d, N)
# print(d)

# 探索順の全組み合わせを試して、最小を見つける
ans = float("inf")
for comb in itertools.permutations(r):
	dist = 0
	for i in range(R-1):
		dist += d[comb[i]-1][comb[i+1]-1]
	ans = min(ans, dist)

print(ans)