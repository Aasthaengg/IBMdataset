N,K=map(int,input().split())
L=list(map(int,input().split()))
L.sort();
ans = int(0)
for i in range(N-K,N):
	ans+=L[i]
print(ans)