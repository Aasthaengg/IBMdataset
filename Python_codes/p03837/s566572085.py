n,m = map(int,input().split())

dist = [[10**10 for i in range(n)]for j in range(n)]
for i in range(n):
	dist[i][i] == 0

a = [0]*m
b = [0]*m
c = [0]*m

for i in range(m):
	a[i], b[i], c[i] = map(int,input().split())
	dist[a[i]-1][b[i]-1] = c[i]
	dist[b[i]-1][a[i]-1] = c[i]


#nは頂点、mは辺、a、bは頂点、cはaとbの距離


for k in range(n):
	for i in range(n):
		for j in range(n):
			dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


res = 0
for i in range(m):
	if c[i] > dist[a[i]-1][b[i]-1]:
		res += 1

print(res)
