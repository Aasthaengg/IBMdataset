H,W=map(int,input().split())
cost=[list(map(int,input().split())) for _ in range(10)]

def dijkstra(S,N,cost):
	d = [float("inf")]*N
	used = [False]*N
	d[S] = 0
	
	while True:
		v = -1
		for i in range(N):
			if (not used[i]) and (v == -1):
				v = i
			elif (not used[i]) and d[i] < d[v]:
				v = i
		if v == -1:
			break
		used[v] = True
		
		for j in range(N):
			d[j] = min(d[j], d[v]+cost[v][j])
	
	return d

min_cost=[0]*10
for i in range(10):
    d=dijkstra(i,10,cost)
    min_cost[i]=d[1]

A=[list(map(int,input().split())) for _ in range(H)]
ans=0
for i in range(H):
    for j in range(W):
        if A[i][j]==-1:
            continue
        else:
            ans+=min_cost[A[i][j]]
print(ans)