n,m,x=map(int,input().split())
a=[False]*(n+1)
A=list(map(int,input().split()))
for i in range(m):
	s = A[i]
	a[s] = True

print(min(sum(a[:x]), sum(a[x:])))