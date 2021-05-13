n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]
h.sort()
INF=2*10**9
ans=INF
for i in range(n-k+1):
	diff=h[i+k-1]-h[i]
	if ans>diff:
		ans=diff
		if ans==0:
			print(0)
			exit()
print(ans)