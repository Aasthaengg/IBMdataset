n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
h.sort()
ans=float("inf")
for i in range(len(h)-k+1):
	ma = h[i+k-1]
	mi = h[i]
	ans = min(ans,ma-mi)

print(ans)