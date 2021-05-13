h, w, d = map(int, input().split())
a = []
dict = {}
for i in range(h):
	b = list(map(int, input().split()))
	for j in range(w):
		dict[b[j]] = [i,j]

dist = [0 for i in range(h*w)]
for i in range(1,h*w-d+1):
	dist[i-1] = abs(dict[i+d][1]-dict[i][1]) + abs(dict[i+d][0]-dict[i][0])

for i in range(h*w-d-1,-1,-1):
	dist[i] += dist[i+d]

q = int(input())
for i in range(q):
	l, r = map(int, input().split())
	ans = dist[l-1] - dist[r-1]
	print (ans)
