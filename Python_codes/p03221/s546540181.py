import bisect
n,m=map(int,input().split())
k=[[] for _ in range(n)]
p=[0 for _ in range(m)]
y=[0 for _ in range(m)]
for i in range(m):
	a,b = map(int,input().split())
	y[i] = b
	p[i] = a
	k[a-1].append(b)
for i in range(n):
	k[i].sort()
ansl = []
for i in range(m):
	d1 = str(p[i]).zfill(6)
	d2 = str(bisect.bisect_right(k[p[i]-1], y[i])).zfill(6)
	ansl.append(d1+d2)
print("\n".join(ansl))