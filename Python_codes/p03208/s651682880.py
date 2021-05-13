N,K=map(int,input().split())
h=[int(input())for _ in range(N)]
h.sort()
ans=10**10
for i in range(N-K+1):
	tmp=h[i+K-1]-h[i]
	if tmp<ans:
		ans=tmp
print(ans)