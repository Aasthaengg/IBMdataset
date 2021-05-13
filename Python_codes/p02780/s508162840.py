N,K=map(int, input().split())
P=list(map(int, input().split()))
saikoro=[1+0.5*sai for sai in range(1000)]

ruiseki=0
for i in range(K):
	ruiseki+=saikoro[P[i]-1]

ans=ruiseki
for k in range(N-K):
	ruiseki=ruiseki-saikoro[P[k]-1]+saikoro[P[K+k]-1]
	ans=max(ans,ruiseki)
	
print(ans)